/* Letter Castle service worker — keeps the game playable offline. */
const CACHE = 'letter-castle-v10';
const ASSETS = ['./', './index.html', './record.html', './manifest.json', './icon.svg'];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE)
      .then(c => c.addAll(ASSETS))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);

  // Page loads: network first (so updates arrive), fall back to the right cached page.
  if (req.mode === 'navigate') {
    const pageKey = url.pathname.endsWith('record.html') ? './record.html' : './index.html';
    e.respondWith(
      fetch(req)
        .then(res => {
          const copy = res.clone();
          caches.open(CACHE).then(c => c.put(pageKey, copy));
          return res;
        })
        .catch(() => caches.match(pageKey))
    );
    return;
  }

  // Cache-busted requests (?b=..., ?studio=...): network only, fall back to the
  // plain cached copy when offline — and never pollute the cache with variants.
  if (url.search) {
    e.respondWith(
      fetch(req).catch(() => caches.match(url.origin + url.pathname))
    );
    return;
  }

  // Everything else (incl. sounds/*): cached copy immediately, refresh in background.
  e.respondWith(
    caches.match(req).then(hit => {
      const net = fetch(req)
        .then(res => {
          if (res && res.ok) {
            const copy = res.clone();
            caches.open(CACHE).then(c => c.put(req, copy));
          }
          return res;
        })
        .catch(() => hit);
      return hit || net;
    })
  );
});
