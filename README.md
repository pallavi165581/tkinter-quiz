# Quiz Master

A timed multiple-choice quiz app built with **tkinter** — frontend only,
no backend, no database. All data lives in memory.

## Features

- 10 multiple-choice questions, 15 seconds each
- Instant green/red feedback on answers
- Final score screen with percentage and replay option
- Dark-themed UI in ~110 lines

## Run

```bash
python3 quiz_app.py
```

On macOS, prefer a modern Python (Tk 8.6+) — e.g. Homebrew Python:

```bash
/opt/homebrew/bin/python3.14 quiz_app.py
```

The macOS system Python (`/usr/bin/python3`) ships Tk 8.5, which renders
garbled/overlapping UI on recent macOS versions.
