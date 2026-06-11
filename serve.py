#!/usr/bin/env python3
"""Letter Castle server.

Serves the game folder like `python -m http.server`, and additionally lets
the Sound Studio (record.html) save parent-recorded letter sounds into the
sounds/ folder. Recording endpoints only accept requests from this computer
(localhost); phones and tablets just play the saved files.

Usage: python serve.py [port]   (default port 8000)
"""
import json
import os
import re
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

ROOT = os.path.dirname(os.path.abspath(__file__))
SOUNDS = os.path.join(ROOT, 'sounds')
NAME_RE = re.compile(r'^[a-z0-9-]{1,16}$')
AUDIO_EXT = {
    'audio/webm': 'webm',
    'audio/ogg': 'ogg',
    'audio/mp4': 'm4a',
    'audio/mpeg': 'mp3',
    'audio/wav': 'wav',
}
MAX_BYTES = 5 * 1024 * 1024


class Handler(SimpleHTTPRequestHandler):
    def _is_local(self):
        return self.client_address[0] in ('127.0.0.1', '::1')

    def _json(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_body(self):
        try:
            n = int(self.headers.get('Content-Length') or 0)
        except ValueError:
            return None
        if n <= 0 or n > MAX_BYTES:
            return None
        return self.rfile.read(n)

    def end_headers(self):
        # recordings change in place: let browsers revalidate them
        if urlparse(self.path).path.startswith('/sounds/'):
            self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

    def do_GET(self):
        if urlparse(self.path).path == '/ping':
            return self._json(200, {'ok': True, 'studio': self._is_local()})
        return super().do_GET()

    def do_POST(self):
        if not self._is_local():
            return self._json(403, {'ok': False, 'error': 'recording only works on the computer running the server'})
        url = urlparse(self.path)
        os.makedirs(SOUNDS, exist_ok=True)

        if url.path == '/save-sound':
            name = (parse_qs(url.query).get('name') or [''])[0]
            ctype = (self.headers.get('Content-Type') or '').split(';')[0].strip()
            ext = AUDIO_EXT.get(ctype)
            if not NAME_RE.match(name) or not ext:
                return self._json(400, {'ok': False, 'error': 'bad name or audio type'})
            body = self._read_body()
            if body is None:
                return self._json(400, {'ok': False, 'error': 'empty or too large'})
            for other in AUDIO_EXT.values():  # keep one file per sound
                if other != ext:
                    p = os.path.join(SOUNDS, '%s.%s' % (name, other))
                    if os.path.exists(p):
                        os.remove(p)
            fname = '%s.%s' % (name, ext)
            with open(os.path.join(SOUNDS, fname), 'wb') as f:
                f.write(body)
            return self._json(200, {'ok': True, 'file': fname})

        if url.path == '/save-manifest':
            body = self._read_body()
            try:
                data = json.loads(body or b'')
            except ValueError:
                data = None
            if not isinstance(data, dict):
                return self._json(400, {'ok': False, 'error': 'bad json'})
            with open(os.path.join(SOUNDS, 'manifest.json'), 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=1)
            return self._json(200, {'ok': True})

        return self._json(404, {'ok': False, 'error': 'unknown endpoint'})

    def do_DELETE(self):
        if not self._is_local():
            return self._json(403, {'ok': False})
        url = urlparse(self.path)
        if url.path == '/delete-sound':
            name = (parse_qs(url.query).get('name') or [''])[0]
            if not NAME_RE.match(name):
                return self._json(400, {'ok': False})
            removed = []
            for ext in AUDIO_EXT.values():
                p = os.path.join(SOUNDS, '%s.%s' % (name, ext))
                if os.path.exists(p):
                    os.remove(p)
                    removed.append('%s.%s' % (name, ext))
            return self._json(200, {'ok': True, 'removed': removed})
        return self._json(404, {'ok': False})


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    os.chdir(ROOT)
    srv = ThreadingHTTPServer(('', port), Handler)
    print('Letter Castle server running on http://localhost:%d' % port)
    print('Sound Studio (this computer only): http://localhost:%d/record.html' % port)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
