🎮 MINECRAFT AFK BOT - ULTRA SIMPLE VERSION
==========================================

📥 WHAT YOU NEED:
1. Python 3.8 or higher
2. Discord account
3. Minecraft server IP

🚀 3-STEP SETUP:

STEP 1: Install Python
----------------------
1. Go to: https://www.python.org/downloads/
2. Download Python (Click big yellow button)
3. Run installer
4. CHECK "Add Python to PATH" ✓
5. Click "Install Now"

STEP 2: Get Discord Bot Token
-----------------------------
1. Open: https://discord.com/developers/applications
2. Click "New Application" (top right)
3. Name it "AFK Bot" → Create
4. Click "Bot" on left menu
5. Click "Add Bot" → "Yes, do it!"
6. Click "Copy" under Token
7. Save this token somewhere safe

STEP 3: Get Your Discord ID
---------------------------
1. Open Discord app
2. Click Settings (gear icon)
3. Go to "Advanced"
4. Enable "Developer Mode"
5. Right-click your name in any chat
6. Click "Copy ID"

⚙️ CREATE CONFIG FILE:
1. Create new file named "config.json"
2. Copy-paste this inside:
{
    "discord_token": "PASTE_TOKEN_HERE",
    "admin_id": "PASTE_YOUR_DISCORD_ID",
    "server_ip": "your.server.ip",
    "server_port": 25565,
    "bot_username": "AFK_Bot",
    "command_prefix": "/"
}
3. Replace PASTE_TOKEN_HERE with your token
4. Replace PASTE_YOUR_DISCORD_ID with your ID
5. Replace your.server.ip with your Minecraft server IP

🚀 RUN THE BOT:
1. Open Command Prompt/Terminal
2. Navigate to bot folder:
   cd Desktop/afk-bot
3. Install requirements:
   pip install -r requirements.txt
4. Run the bot:
   python bot.py

🎮 DISCORD COMMANDS:
/help - Show all commands
/joinafk - Start AFK bot (ADMIN ONLY)
/leaveafk - Stop AFK bot (ADMIN ONLY)
/status - Check bot status
/server - Show server info
/players - Show online players
/ping - Check bot latency
/setup - Show this guide again

❓ TROUBLESHOOTING:

Problem: "Invalid token"
Solution: Get new token from Discord Developer Portal

Problem: "Bot not responding"
Solution: Add bot to server with proper permissions

Problem: "Python not found"
Solution: Reinstall Python with "Add to PATH" checked

Problem: "Module not found"
Solution: Run: pip install -r requirements.txt

📞 NEED HELP?
1. Check all steps carefully
2. Make sure token is correct
3. Verify server IP is right
4. Bot needs to be added to your server

✅ WHEN WORKING:
1. Bot shows "Online" in Discord
2. Type /joinafk to start
3. Bot will simulate AFK activities
4. Shows as player on server
5. Auto-reconnects if "disconnected"

🎉 CONGRATULATIONS!
You now have a working AFK bot!
