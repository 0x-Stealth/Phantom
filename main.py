import discord
from discord.ext import commands
from discord import Intents
import modules.cookies as cumkies

intents = Intents.all() # can we go back to the days where there was no intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'i am {bot.user.name}')

@bot.command()
async def cookies(ctx):
    content = cumkies.main_func()  # get the content from main_func
    await ctx.send(content)  

if __name__ == "__main__":
    with open('token.txt', 'r') as file:
        bot_token = file.read().strip()
    bot.run(bot_token)

