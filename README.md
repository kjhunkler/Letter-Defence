# Letter Castle 🏰

A tower-defense letter game for little learners. Letter troops march down a country
road toward your castle — find the matching letter to launch a catapult rock and
stop them before they sneak through the gate and steal a snack — sheep, bread,
cheese, pie, pumpkins… a different mix of 14 farm treats fills the paddock each game.

## How to run

Everything is one file with no internet needed.

- **Easiest (hosts on your PC):** double-click `serve.bat`. It starts a Python web
  server, opens http://localhost:8000 in your browser, and prints the address to type
  on a phone or tablet on the same Wi-Fi (e.g. `http://192.168.x.x:8000`). Keep the
  window open while playing; close it to stop. The first time, Windows Firewall may
  ask — choose **Allow** on private networks so phones can connect.
- **Manual:** `python serve.py` in this folder, then open `http://localhost:8000`
  (plain `python -m http.server 8000` also works for playing, but can't save
  Sound Studio recordings).
- **No server at all:** double-click `index.html`, or copy it onto the device and
  open it in any browser (add to home screen for a full-screen feel).
- **Dev preview:** `.claude/launch.json` runs the same server on port 8123 for
  Claude Code's preview panel (separate port, so both can run at once).

## Game modes

| Mode | What the child does |
|---|---|
| **Campaign** (default) | A journey through the other modes, one stage per round: B→b with 3 then 4 choices, b→B with 4 then 5, then First Sounds with lowercase (3) and uppercase (4) answers. Progress is remembered between sessions, and the stage plan is fully editable in settings (add/remove stages, any mode/style/choice count) |
| **Letter Match** | A troop carries a letter (e.g. `b`) — tap the matching uppercase `B` |
| **Letter Teams** | Two-letter pairs: digraphs (sh, ch, th…) and blends (st, br…) |
| **First Sounds** | A troop carries a picture (🐶) — the voice asks "What letter makes the sound at the beginning of Dog?" (answers show lowercase by default; uppercase or both available) |
| **Word Builder** | A word sign shows ghost letters (🐱 c‑a‑t) — each defeated troop drops its letter into the next slot; finishing a word earns a bonus ⭐ |
| **Numbers** | The troop carries a banner of pictures (🐢🐢🐢🐢🐢) — count them and tap the numeral; the voice counts back "1, 2, 3, 4, 5! Five turtles!" |

The game also **adapts quietly**: letters the child misses show up a little more
often (and mastered ones rest), in every mode — Word Builder even prefers words
containing the tricky letters.

## How a turn works

1. A troop marches in from the left, over the bridge, toward the castle gate.
2. The child picks from 2–5 choices (parent-configurable).
3. **Correct** → the catapult fires, bonks the troop (+1 ⭐, +2 on the first try),
   and a little worker loads the next rock.
4. **Wrong** → the rock misses (sometimes splashing into the stream!), that choice is
   disabled, and the troop marches one step closer.
5. If a troop reaches the gate it slips inside, runs off with a snack from the
   paddock, and when the paddock is empty the round ends.

## Star Shop ⭐

Stars earned by defeating troops are spendable! The **⭐ Star Shop** button on the
title screen (and after each round) lets the child decorate the castle:

| Item | Cost | What it does |
|---|---|---|
| 🎀 Party Bunting | 8 ⭐ | Cheerful flags strung across the wall |
| 🌈 Rainbow Flags | 12 ⭐ | Replaces the tower pennants, adds a third |
| 🌻 Castle Garden | 18 ⭐ | Sunflowers, blossoms and potted plants |
| 👑 Royal Banners | 25 ⭐ | Star banners flanking the gate |
| 🐲 Pet Dragon | 40 ⭐ | Perches on the keep (blinks, puffs smoke) — and **once per round** swoops down to scare away a troop that's one step from the gate |

Purchases are permanent and saved on the device; owned items can be switched
on/off in the shop. The dragon only needs to help on Steady/Brave difficulty —
on Relaxed he's just good company.

## Parent-recorded letter sounds (Sound Studio) 🎙️

You can replace the robot voice's letter sounds with **your own voice**:

1. Start the game with `serve.bat` on the computer.
2. Open **http://localhost:8000/record.html** (also linked from the grown-ups
   settings → "Open the Sound Studio").
3. For each letter (and the sh/ch/th… teams), tap ●, say the letter's **sound**
   ("buh" for B, "sss" for S), and it saves automatically.

Recordings are plain audio files stored in the **sounds/** folder next to the game
(`b.webm`, `sh.webm`, … listed in `sounds/manifest.json`), so they sync with the
folder (OneDrive) and survive reinstalls. The game plays your voice whenever a
letter is announced — before the robot voice, or alone if the voice is off — on
**every** device, and offline once cached.

Notes: browsers only allow the microphone on the computer itself (localhost), so
record on the PC; phones and tablets play the files just fine. The "Parent letter
sounds" switch in settings turns playback on/off.

## Grown-ups settings (🔒 button, multiplication gate)

- Game mode, matching style (b→B, B→b, B→B, b→b, or mixed)
- Campaign plan editor: per-stage mode, style and choice count; reset plan; jump back to stage 1
- Which letters / letter teams are in play (tap to toggle, quick presets)
- Word Builder word length: short (3), longer (4), or both
- First Sounds answer buttons: lowercase (default), uppercase, or both (Aa)
- Numbers counting range: 1–3, 1–5 (default), or 1–10
- Choices per question (2–5)
- Difficulty: **Relaxed** (can't lose), **Steady** (the default — steal only if every
  guess is wrong), **Brave** (troops start close)
- Round length (5/8/12 troops), paddock size (3/5/8 snacks)
- Sound effects and voice on/off (voice uses the device's built-in speech)
- Parent letter sounds on/off, plus a link to the Sound Studio recorder
- Progress: tricky-letter report, first-try accuracy, reset button

Settings and progress are saved on the device (localStorage).

## Idea backlog

- Boss troops that need two correct answers; golden bonus troops
- Timed marching option for older kids (troops walk continuously)
- Seasonal themes: snow, autumn, nighttime with torches
- Dyslexia-friendly font toggle and colorblind-safe palette option
- Per-letter mastery heatmap for parents, exportable
