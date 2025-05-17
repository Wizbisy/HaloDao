import discord
from discord.ext import commands
import random
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
if not TOKEN:
    print("Error: DISCORD_TOKEN is not set in the environment.")
    exit(1)

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

jokes = [
    "Why did the programmer prefer dark mode? Because the light attracted bugs!",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why don’t skeletons fight each other? They don’t have the guts!",
    "What’s a robot’s favorite snack? Microchips!",
    "Why did the coffee file a police report? It got mugged!"
]

quotes = [
    "The best way to predict the future is to create it. – Peter Drucker",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "You are never too old to set another goal or to dream a new dream. – C.S. Lewis"
]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} at 07:04 PM WAT, May 17, 2025')

@bot.command()
async def joke(ctx):
    print(f"Command !joke received from {ctx.author} in channel {ctx.channel.id}")
    if ctx.guild and ctx.guild.id == 937472470796079135:
        joke = random.choice(jokes)
        await ctx.send(f"**Here’s a joke for you:** {joke}")
    else:
        await ctx.send("This command is only available in the HaloDao server!")

@bot.command()
async def inspire(ctx):
    if ctx.guild and ctx.guild.id == 937472470796079135:
        quote = random.choice(quotes)
        await ctx.send(f"**Here’s some inspiration:** {quote}")
    else:
        await ctx.send("This command is only available in the HaloDao server!")

bot.run(TOKEN)
