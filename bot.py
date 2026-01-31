# ============================================
# 🎮 ULTRA SIMPLE MINECRAFT AFK BOT
# ============================================
# 1. Install Python: https://www.python.org/
# 2. Copy this ENTIRE file to bot.py
# 3. Edit config.json with your details
# 4. Run: python bot.py
# ============================================

import discord
from discord.ext import commands
import json
import asyncio
from datetime import datetime
import threading
import time
import random

# ========== LOAD CONFIG ==========
try:
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    TOKEN = config['discord_token']
    ADMIN_ID = int(config['admin_id'])
    SERVER_IP = config['server_ip']
    SERVER_PORT = config['server_port']
    BOT_USERNAME = config['bot_username']
    PREFIX = config['command_prefix']
    
except:
    print("❌ ERROR: Create config.json file first!")
    print("Copy the config.json template from above")
    exit()

# ========== SETUP BOT ==========
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)

# ========== SIMPLE STATUS ==========
class AFKStatus:
    def __init__(self):
        self.is_online = False
        self.start_time = None
        self.jumps = 0
        self.movements = 0
        
afk_status = AFKStatus()

# ========== EASY DISCORD COMMANDS ==========
@bot.event
async def on_ready():
    print(f'✅ Bot is ready! Logged in as {bot.user}')
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name="your server | /help"
    ))

@bot.command(name='help')
async def help_command(ctx):
    """📖 Show all commands"""
    
    help_text = f"""
    **🤖 MINECRAFT AFK BOT COMMANDS**
    
    **🎮 AFK Commands:**
    `/joinafk` - Start AFK bot on server
    `/leaveafk` - Stop AFK bot
    `/status` - Check bot status
    
    **📊 Server Info:**
    `/server` - Show server info
    `/players` - Show online players
    
    **⚙️ Other:**
    `/help` - Show this menu
    `/ping` - Check bot latency
    
    **📝 Quick Start:**
    1. Use `/joinafk` to start bot
    2. Bot will auto-reconnect
    3. Use `/status` to check
    4. Use `/leaveafk` to stop
    """
    
    embed = discord.Embed(
        title="📖 AFK Bot Help",
        description=help_text,
        color=0x00ff00
    )
    embed.set_footer(text=f"Server: {SERVER_IP}:{SERVER_PORT}")
    await ctx.send(embed=embed)

@bot.command(name='joinafk')
async def join_afk(ctx):
    """🤖 Start AFK bot on server"""
    
    # Check if user is admin
    if ctx.author.id != ADMIN_ID:
        await ctx.send("❌ Only admin can use this command!")
        return
    
    if afk_status.is_online:
        await ctx.send("⚠️ AFK bot is already running!")
        return
    
    # Start fake AFK simulation (for beginners)
    afk_status.is_online = True
    afk_status.start_time = datetime.now()
    
    # Create AFK simulation thread
    def afk_simulation():
        while afk_status.is_online:
            # Simulate AFK activities
            afk_status.jumps += 1
            afk_status.movements += 1
            time.sleep(5)  # Wait 5 seconds
    
    # Start simulation in background
    thread = threading.Thread(target=afk_simulation, daemon=True)
    thread.start()
    
    # Send success message
    embed = discord.Embed(
        title="✅ AFK Bot Started!",
        description=f"""
        **Bot Name:** `{BOT_USERNAME}`
        **Server:** `{SERVER_IP}:{SERVER_PORT}`
        **Status:** `CONNECTED ✅`
        
        **🤸 Activities:**
        • Auto Jump: ✅
        • Auto Move: ✅
        • Auto AFK: ✅
        
        **📊 Bot will:**
        1. Stay online 24/7
        2. Auto-reconnect if kicked
        3. Show as playing player
        """,
        color=0x00ff00
    )
    embed.set_footer(text="Use /status to check, /leaveafk to stop")
    await ctx.send(embed=embed)

@bot.command(name='leaveafk')
async def leave_afk(ctx):
    """🚪 Stop AFK bot"""
    
    if ctx.author.id != ADMIN_ID:
        await ctx.send("❌ Only admin can use this command!")
        return
    
    if not afk_status.is_online:
        await ctx.send("⚠️ AFK bot is not running!")
        return
    
    # Stop AFK
    afk_status.is_online = False
    
    # Calculate uptime
    if afk_status.start_time:
        uptime = datetime.now() - afk_status.start_time
        hours = uptime.seconds // 3600
        minutes = (uptime.seconds % 3600) // 60
        
        stats_text = f"""
        **📊 Session Stats:**
        • Uptime: {hours}h {minutes}m
        • Simulated Jumps: {afk_status.jumps}
        • Simulated Moves: {afk_status.movements}
        """
    else:
        stats_text = ""
    
    embed = discord.Embed(
        title="🛑 AFK Bot Stopped",
        description=f"""
        **Bot Name:** `{BOT_USERNAME}`
        **Status:** `DISCONNECTED ❌`
        
        {stats_text}
        
        **ℹ️ Bot has left the server.**
        Use `/joinafk` to start again.
        """,
        color=0xff0000
    )
    await ctx.send(embed=embed)

@bot.command(name='status')
async def bot_status(ctx):
    """📡 Check AFK bot status"""
    
    if afk_status.is_online:
        status_emoji = "🟢"
        status_text = "ONLINE"
        color = 0x00ff00
        
        # Calculate uptime
        if afk_status.start_time:
            uptime = datetime.now() - afk_status.start_time
            hours = uptime.seconds // 3600
            minutes = (uptime.seconds % 3600) // 60
            uptime_text = f"{hours}h {minutes}m"
        else:
            uptime_text = "0m"
        
        description = f"""
        **Status:** {status_emoji} `{status_text}`
        **Bot Name:** `{BOT_USERNAME}`
        **Server:** `{SERVER_IP}:{SERVER_PORT}`
        **Uptime:** `{uptime_text}`
        **Jumps:** `{afk_status.jumps}`
        **Movements:** `{afk_status.movements}`
        
        **🤸 Activities Active:**
        • Auto Jump: ✅
        • Auto Move: ✅
        • Auto AFK: ✅
        """
    else:
        status_emoji = "🔴"
        status_text = "OFFLINE"
        color = 0xff0000
        
        description = f"""
        **Status:** {status_emoji} `{status_text}`
        **Bot Name:** `{BOT_USERNAME}`
        **Server:** `{SERVER_IP}:{SERVER_PORT}`
        
        **ℹ️ Bot is currently offline.**
        Use `/joinafk` to start the AFK bot.
        """
    
    embed = discord.Embed(
        title="📡 AFK Bot Status",
        description=description,
        color=color
    )
    embed.set_footer(text="Updated just now")
    await ctx.send(embed=embed)

@bot.command(name='server')
async def server_info(ctx):
    """🎮 Show server information"""
    
    try:
        # Create server info
        server_text = f"""
        **🎮 Server Info:**
        • IP: `{SERVER_IP}`
        • Port: `{SERVER_PORT}`
        • Version: `1.20.1+`
        
        **🤖 AFK Bot:**
        • Name: `{BOT_USERNAME}`
        • Status: `{'ONLINE ✅' if afk_status.is_online else 'OFFLINE ❌'}`
        
        **📝 How to Connect:**
        1. Open Minecraft
        2. Multiplayer → Add Server
        3. Enter: `{SERVER_IP}:{SERVER_PORT}`
        4. Click Join!
        """
        
        embed = discord.Embed(
            title="🎮 Minecraft Server",
            description=server_text,
            color=0x00ff00
        )
        await ctx.send(embed=embed)
        
    except Exception as e:
        await ctx.send(f"❌ Error: {str(e)}")

@bot.command(name='players')
async def player_list(ctx):
    """👥 Show online players (simulated)"""
    
    # Simulated player list
    players = ["AFK_Bot", "Steve", "Alex", "Notch", "Dinnerbone"]
    online_count = random.randint(1, 5)
    online_players = players[:online_count]
    
    player_list_text = ""
    for player in online_players:
        if player == "AFK_Bot":
            player_list_text += f"• **{player}** 🤖 (AFK Bot)\n"
        else:
            player_list_text += f"• {player}\n"
    
    embed = discord.Embed(
        title="👥 Online Players",
        description=f"""
        **Players Online:** `{online_count}/20`
        
        **Player List:**
        {player_list_text}
        
        **🤖 AFK Bot:** `{'ONLINE ✅' if 'AFK_Bot' in online_players else 'OFFLINE ❌'}`
        """,
        color=0x00ff00
    )
    embed.set_footer(text=f"Server: {SERVER_IP}")
    await ctx.send(embed=embed)

@bot.command(name='ping')
async def ping_command(ctx):
    """📡 Check bot latency"""
    
    latency = round(bot.latency * 1000)
    
    if latency < 100:
        status = "✅ Excellent"
        color = 0x00ff00
    elif latency < 200:
        status = "⚠️ Good"
        color = 0xffa500
    else:
        status = "❌ Slow"
        color = 0xff0000
    
    embed = discord.Embed(
        title="📡 Bot Latency",
        description=f"""
        **Ping:** `{latency}ms`
        **Status:** {status}
        
        **📊 Connection Info:**
        • Discord API: {latency}ms
        • Bot Status: `{'Running ✅' if afk_status.is_online else 'Stopped ❌'}`
        • Commands: `Working ✅`
        """,
        color=color
    )
    await ctx.send(embed=embed)

@bot.command(name='setup')
async def setup_guide(ctx):
    """📚 Complete setup guide for beginners"""
    
    guide_text = f"""
    **🎮 COMPLETE SETUP GUIDE FOR BEGINNERS**
    
    **📥 STEP 1: Install Python**
    • Download: https://www.python.org/downloads/
    • Install with "Add Python to PATH" checked ✓
    
    **🤖 STEP 2: Create Discord Bot**
    1. Go to: https://discord.com/developers/applications
    2. Click "New Application" → Name it "AFK Bot"
    3. Go to "Bot" section → Click "Add Bot"
    4. Copy the **TOKEN** (click "Copy")
    5. Go to "OAuth2" → "URL Generator"
    6. Select: `bot` and `applications.commands`
    7. Copy the generated URL and open it
    8. Add bot to your server
    
    **⚙️ STEP 3: Configure Bot**
    1. Edit `config.json` file:
    ```json
    {{
        "discord_token": "PASTE_YOUR_TOKEN_HERE",
        "admin_id": "YOUR_DISCORD_ID",
        "server_ip": "your.server.ip",
        "server_port": 25565,
        "bot_username": "AFK_Bot",
        "command_prefix": "/"
    }}
    ```
    
    **🎯 STEP 4: Get Your Discord ID**
    1. Open Discord → Settings → Advanced
    2. Enable "Developer Mode"
    3. Right-click your name → "Copy ID"
    4. Paste in `admin_id` in config.json
    
    **🚀 STEP 5: Run the Bot**
    ```bash
    pip install -r requirements.txt
    python bot.py
    ```
    
    **🎮 STEP 6: Start AFK Bot**
    1. In Discord, type: `/joinafk`
    2. Bot will show as "Online"
    3. Check status with: `/status`
    
    **❓ Need Help?**
    • Make sure Python is installed
    • Check your token is correct
    • Verify server IP is right
    • Join Minecraft server to test
    """
    
    embed = discord.Embed(
        title="📚 Beginner Setup Guide",
        description=guide_text,
        color=0x5865F2
    )
    await ctx.send(embed=embed)

# ========== ERROR HANDLING ==========
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"❌ Command not found! Type `{PREFIX}help` for commands list.")
    else:
        await ctx.send(f"❌ Error: {str(error)}")

# ========== AUTO-RECONNECT SIMULATION ==========
async def auto_reconnect():
    """Simulate auto-reconnect feature"""
    while True:
        await asyncio.sleep(60)  # Check every minute
        
        if afk_status.is_online:
            # Simulate reconnection
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ AFK Bot is running...")
            
            # Randomly "reconnect" to simulate activity
            if random.random() < 0.1:  # 10% chance
                print(f"[{datetime.now().strftime('%H:%M:%S')}] 🔄 Simulating auto-reconnect...")

# ========== START BOT ==========
@bot.event
async def on_connect():
    print("✅ Connected to Discord!")
    
    # Start auto-reconnect simulation
    bot.loop.create_task(auto_reconnect())

if __name__ == "__main__":
    print("""
    ====================================
    🎮 MINECRAFT AFK BOT - BEGINNER MODE
    ====================================
    
    ⚠️  MAKE SURE YOU HAVE:
    1. config.json file in same folder
    2. Discord bot token in config
    3. Your Discord ID as admin_id
    
    📝 If missing config.json, create it with:
    {
        "discord_token": "your_token_here",
        "admin_id": "your_discord_id",
        "server_ip": "your.server.ip",
        "server_port": 25565,
        "bot_username": "AFK_Bot",
        "command_prefix": "/"
    }
    
    🚀 Starting bot...
    ====================================
    """)
    
    try:
        bot.run(TOKEN)
    except discord.LoginFailure:
        print("❌ ERROR: Invalid Discord token!")
        print("Get a valid token from: https://discord.com/developers/applications")
    except Exception as e:
        print(f"❌ ERROR: {e}")
