import os
import nextcord
from nextcord.ext import commands


intents = nextcord.Intents().all()
bot = commands.Bot(intents=intents)
bot.remove_command("help")


@bot.event
async def on_ready():
  print('Logged in as')
  print(bot.user.name)
  print(bot.user.id)
  print('------')
  print(len(bot.guilds))

def get_bot():
    return bot

for file in os.listdir("./cogs/commands"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.commands.{name}")

for file in os.listdir("./cogs/events"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.events.{name}")

bot.run('MTA3NzMyMzc2Mzg4MTg3MzQ1OQ.G4exGA.IWQoL662HJZx3CJLAOcBoi2WFWlNrf2awpkHwY')
