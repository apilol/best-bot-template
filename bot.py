import discord
from discord.ext import commands

# ------------------------------------------------------- # Create Instance
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='>', intents=intents)
# ------------------------------------------------------- # Configuration
Logging = True # True or False
token = 'input bot token'
settings = json.load(open("settings.json", encoding="utf-8"))
def staff(ctx):
    return str(ctx.author.id) in settings["staffId"]
# ------------------------------------------------------- # Commands
@bot.slash_command(description="Pong!")
async def ping(ctx):
  if not staff(ctx): # If Not Staff, Will return Error
    await ctx.respond(f"Error!", delete_after=3.0)
  else:
    await ctx.respond(f"Pong!")
    if Logging == True: # If Logging = True, It will log commmand
      await bot.get_channel(logging channel id).send(f"Ping Command has Been Run By: {ctx.author.mention}")
    else:
      pass # If Logging = False, Bot Will End Command
    
bot.run(token)
