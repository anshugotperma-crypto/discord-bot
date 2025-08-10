import os
from keep_alive import keep_alive
import discord
from discord.ext import commands

# Start the keep-alive web server (for Replit + UptimeRobot)
keep_alive()

TOKEN = os.getenv("DISCORD_TOKEN")  # Set this in Replit Secrets

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix=None, intents=intents)  # No prefix; responds to messages

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")

@bot.event
async def on_message(message):
    # ignore bots (including itself)
    if message.author.bot:
        return

    content = message.content.lower().strip()

    # If message contains 'ip' (anywhere), respond with the SMP info
    if "ip" in content:
        await message.channel.send(
            "👑 **WLC TO SRUSHTI SMP**\n"
            "🖥️ Java IP: `srushtismp.hs.vc` ✅\n"
            "📱 Bedrock IP: `srushtismp.hs.vc` | Port: `19132`\n"
            "|| @everyone @here ||"
        )

# Run the bot
if not TOKEN:
    print("ERROR: DISCORD_TOKEN environment variable not set.")
else:
    bot.run(TOKEN)
