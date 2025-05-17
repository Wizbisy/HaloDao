import discord
from discord.ext import commands, tasks
import random
from dotenv import load_dotenv
import os

# Load the token from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up the bot with ! prefix
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Lists for jokes and quotes
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

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} at 06:29 PM WAT, May 17, 2025')
    active_message.start()

@tasks.loop(seconds=30)
async def active_message():
    server_id = 937472470796079135  
    channel_id = 1351711239079727185  
    server = bot.get_guild(server_id)
    if server:
        channel = bot.get_channel(channel_id)
        if channel:
            await channel.send("HaIDao is active! Use !joke for a laugh or !inspire for motivation! (Last updated: 06:29 PM WAT, May 17, 2025)")
        else:
            print(f"Channel {channel_id} not found in server {server_id}")
    else:
        print(f"Server {server_id} not found")

# Ensure the task waits for the bot to be ready
@active_message.before_loop
async def before_active_message():
    await bot.wait_until_ready()

# Command: !joke sends a random joke
@bot.command()
async def joke(ctx):
    if ctx.guild and ctx.guild.id == 937472470796079135:
        joke = random.choice(jokes)
        await ctx.send(f"**Here’s a joke for you:** {joke}")
    else:
        await ctx.send("This command is only available in the HaIDao server!")

# Command: !inspire sends a motivational quote
@bot.command()
async def inspire(ctx):
    if ctx.guild and ctx.guild.id == 937472470796079135:
        quote = random.choice(quotes)
        await ctx.send(f"**Here’s some inspiration:** {quote}")
    else:
        await ctx.send("This command is only available in the HaIDao server!")

# Run the bot
bot.run(TOKEN)
