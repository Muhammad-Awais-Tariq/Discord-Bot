import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename="Discord.log" , encoding="utf-8" , mode="w")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("ready")

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server {member.name}")       #to send them the message privatly

@bot.event
async def on_message(message): # it will trigger for any message
    if message.author == bot.user:
        return
    
    if "shit" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} Do not use that word")
    
    await bot.process_commands(message) # allows continuing handling all the message we want it to process continue message

@bot.command() # used to create the custom commands now whenever we will do !hello it will send hello name
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention} !")

bot.run(token,log_handler=handler,log_level=logging.DEBUG)