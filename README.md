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
- **Manual:** `python -m http.server 8000` in this folder, then open
  `http://localhost:8000`.
- **No server at all:** double-click `index.html`, or copy it onto the device and
  open it in any browser (add to home screen for a full-screen feel).
- **Dev preview:** `.claude/launch.json` runs the same server on port 8123 for
  Claude Code's preview panel (separate port, so both can run at once).

## Game modes

| Mode | What the child does |
|---|---|
| **Letter Match** | A troop carries a letter (e.g. `b`) — tap the matching uppercase `B` |
| **Letter Teams** | Two-letter pairs: digraphs (sh, ch, th…) and blends (st, br…) |
| **First Sounds** | A troop carries a picture (🐶) — the voice asks "What letter makes the sound at the beginning of Dog?" (answers show lowercase by default; uppercase or both available) |
| **Word Builder** | A word sign shows ghost letters (🐱 c‑a‑t) — each defeated troop drops its letter into the next slot; finishing a word earns a bonus ⭐ |

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

## Grown-ups settings (🔒 button, multiplication gate)

- Game mode, matching style (b→B, B→b, B→B, b→b, or mixed)
- Which letters / letter teams are in play (tap to toggle, quick presets)
- Word Builder word length: short (3), longer (4), or both
- First Sounds answer buttons: lowercase (default), uppercase, or both (Aa)
- Choices per question (2–5)
- Difficulty: **Relaxed** (can't lose), **Steady** (the default — steal only if every
  guess is wrong), **Brave** (troops start close)
- Round length (5/8/12 troops), paddock size (3/5/8 snacks)
- Sound effects and voice on/off (voice uses the device's built-in speech)
- Progress: tricky-letter report, first-try accuracy, reset button

Settings and progress are saved on the device (localStorage).

## Idea backlog

- Boss troops that need two correct answers; golden bonus troops
- Number mode: count the emojis, pick the numeral (same engine)
- Parent-recorded audio for letter *sounds* (phonics) instead of letter names
- Timed marching option for older kids (troops walk continuously)
- Seasonal themes: snow, autumn, nighttime with torches
- Dyslexia-friendly font toggle and colorblind-safe palette option
- Per-letter mastery heatmap for parents, exportable
