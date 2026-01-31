#!/bin/bash
echo "🎮 Minecraft AFK Bot Installer"
echo "=============================="

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found!"
    echo "Install from: https://www.python.org/downloads/"
    exit 1
fi

echo "✅ Python found"

# Install requirements
echo "Installing requirements..."
pip3 install discord.py mcstatus

# Create config if missing
if [ ! -f "config.json" ]; then
    echo '{
    "discord_token": "YOUR_TOKEN_HERE",
    "admin_id": "YOUR_DISCORD_ID",
    "server_ip": "play.example.com",
    "server_port": 25565,
    "bot_username": "AFK_Bot",
    "command_prefix": "/"
}' > config.json
    echo "⚠️ Created config.json - Please edit it!"
fi

echo ""
echo "🎉 INSTALLATION COMPLETE!"
echo ""
echo "📝 Quick Start:"
echo "1. nano config.json  # Edit with your details"
echo "2. python3 bot.py    # Run the bot"
echo "3. Type /help in Discord"
echo ""
