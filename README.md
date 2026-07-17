# YT Downloader Bot

Telegram bot to download videos/playlists from YouTube, Instagram, TikTok, Twitter, Facebook, Vimeo, SoundCloud etc using yt-dlp + Pyrofork. WZML-X style quality picker with per-format bitrate selection.

## Features

- Video & playlist download with inline quality picker
- Playlist: download all / select range / thumbnails only
- Audio export: MP3 (64/128/192/320K), AAC, FLAC, M4A, OPUS, VORBIS, WAV
- Live progress bar for download + upload
- MongoDB-backed cookies — update `cookies.txt` remotely via bot PM, no redeploy needed
- Koyeb/Heroku ready health-check server

## Environment Variables

| Var | Required | Description |
|---|---|---|
| `API_ID` | ✅ | Telegram API ID (my.telegram.org) |
| `API_HASH` | ✅ | Telegram API Hash |
| `BOT_TOKEN` | ✅ | Bot token from @BotFather |
| `ADMINS` | ✅ | Space-separated Telegram user IDs allowed to update cookies |
| `MONGO_URI` | optional | MongoDB connection string, enables cookie sync |
| `PROXY_URL` | optional | HTTP/SOCKS proxy for yt-dlp |
| `PORT` | optional | Health-check port (default `8000`) |

## Cookies Setup

1. Export `cookies.txt` (Netscape format) from your browser.
2. Send it as a document to the bot in a private chat — only works if your user ID is in `ADMINS`.
3. Bot saves it locally and uploads to MongoDB (if `MONGO_URI` set), so it survives redeploys/restarts.
4. On every boot, bot loads cookies from MongoDB automatically if present.

## Deploy

### Docker / Koyeb

```bash
docker build -t yt-bot .
docker run -e API_ID=xxx -e API_HASH=xxx -e BOT_TOKEN=xxx -e ADMINS="123456" -e MONGO_URI="mongodb+srv://..." yt-bot
```

### Heroku

Uses `heroku.yml` (container stack). Set the same env vars in app settings, then:

```bash
heroku stack:set container
git push heroku main
```

## Commands

- `/start` — intro + supported sites
- `/help` — usage guide
- `/ping` — uptime, cookies status, MongoDB status, proxy status

## Local Run

```bash
pip install -r requirements.txt
export API_ID=xxx API_HASH=xxx BOT_TOKEN=xxx ADMINS="123456"
python3 main.py
```
