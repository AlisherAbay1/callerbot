# Callerbot
![Python](https://img.shields.io/badge/python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Tired of tagging people one by one? This bot does it for you.
Send `/all` — everyone who opted in gets tagged. That's it.

## Features

- `/all` — tags everyone who opted in
- `/reg` / `/unreg` — join or leave the tag list
- `/setme` / `/unsetme` — attach a personal emoji to your mention
- Global preferences via DM — set defaults across all chats
- Local chat settings override global ones
- `/getsettings` — view your current global and local config

## Self-hosting 

1. Clone repository.
```bash
   git clone https://github.com/AlisherAbay1/callerbot
   cd callerbot
```
2. Install dependencies:
```bash
   uv sync
```

3. Create `.env`. Check `.env.example`.
4. Edit `config.toml`.
5. Run:
```bash
   uv run python -m callerbot.main
```
