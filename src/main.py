import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")

intents =  nextcord.Intents.all()

bot = commands.Bot(
    intents=intents,
    status=nextcord.Status.online,
    activity=nextcord.Game(name="in development!")
)

bot.load_extension('cogs.utilities')

@bot.event
async def on_ready():
    print()
    print(f"Logged in as {bot.user} [{bot.application_id}]")
    print()
     
bot.run(token)