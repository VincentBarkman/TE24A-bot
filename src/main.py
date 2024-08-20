import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Ladda miljövariabler från .env-filen
load_dotenv()

# Hämta token från miljövariabler
TOKEN = os.getenv('DISCORD_TOKEN')

# Definiera intents
intents = discord.Intents.default()
intents.message_content = True  # Detta krävs för att kunna läsa meddelandeinnehåll

# Initiera boten med intents
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f'Inloggad som {bot.user}')

# Ladda kommandon från andra filer
bot.load_extension('src.utils.commands.homework')

# Kör boten
bot.run(TOKEN)

