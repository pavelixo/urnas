from discord.ext.commands import Bot
from discord import Intents
from application.settings import BOT_TOKEN

bot = Bot(intents=Intents.all(), command_prefix=">")

@bot.event
async def on_ready():
    print("Running...")

def main():
    bot.run(token=BOT_TOKEN)