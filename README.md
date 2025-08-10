# Highlight (SMP IP Auto-Responder Bot)

This repository contains a simple Discord bot that auto-responds with your SMP IP message when someone types `ip` (or any message containing the word "ip").
It is prepared to be imported into Replit and kept online 24/7 using UptimeRobot.

## Files
- `main.py` - Main bot code.
- `keep_alive.py` - Small Flask webserver used to keep the Repl alive.
- `requirements.txt` - Python packages required.

## Setup (Replit)
1. Create a Repl on https://replit.com/ (Import from GitHub or upload files).
2. Add a Secret in Replit:
   - Key: `DISCORD_TOKEN`
   - Value: *(your bot token from Discord Developer Portal)*
3. Install packages (Replit usually auto-installs from `requirements.txt`). If needed, run in Shell:
   ```
   pip install -r requirements.txt
   ```
4. Click **Run**. The console should show `✅ Bot is online as <name>` when started.
5. To keep 24/7: go to https://uptimerobot.com/, create a free account and add a new monitor:
   - Type: HTTP(s)
   - URL: `https://<your-repl-username>.<repl-name>.repl.co/` (the URL shown when Repl is running)
   - Interval: 5 minutes
6. UptimeRobot will ping the Repl and keep it awake.

## Notes & Safety
- **Never** expose your bot token publicly. If your token leaks, regenerate it in the Discord Developer Portal.
- This bot responds whenever a message **contains** "ip". If you want exact-match or channel-limited behavior, open an issue or edit `main.py`.

## Quick Hindi Instructions
1. Replit par project banao (Import from GitHub ya files upload karo).
2. Replit Secrets me `DISCORD_TOKEN` daalo.
3. Run karo aur UptimeRobot se URL ping karao (5 min interval).
