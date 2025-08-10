import discord
from discord.ext import commands

TOKEN = "MTQwMzk4NzA1MzkzNDI4MDgwNQ.Ga-Ldy.bg0KPEb6BzyohVcaFe6fPcJA4G4Jph56l4ubyc"  # Your bot token here

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is now online!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if "ip" in message.content.lower():
        msg = (
            "👑 **WLC TO SRUSHTI SMP**\n"
            "🖥️ Java IP: `srushtismp.hs.vc` :white_check_mark:\n"
            "📱 Bedrock IP: `srushtismp.hs.vc` | Port: `19132`\n"
            "|| @everyone @here ||"
        )
        await message.channel.send(msg)

    await bot.process_commands(message)

bot.run("MTQwMzk4NzA1MzkzNDI4MDgwNQ.Ga-Ldy.bg0KPEb6BzyohVcaFe6fPcJA4G4Jph56l4ubyc")

