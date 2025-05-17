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
    "Why did the coffee file a police report? It got mugged!",
    "Why did the scarecrow become a motivational speaker? Because he was outstanding in his field!",
    "What do you call a dinosaur that takes care of its teeth? A Flossiraptor!",
    "Why can’t basketball players go on vacation? Because they would get called for traveling!",
    "What do you call a computer that sings? A Dell with a bell!",
    "Why was the math book sad? It had too many problems!",
    "What did the zero say to the eight? Nice belt!",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "What’s a pirate’s favorite letter? You think it’s R, but it’s the C they love!",
    "Why don’t eggs tell jokes? They’d crack up!",
    "What do you call a sleeping bull? A bulldozer!"
]

quotes = [
    "The best way to predict the future is to create it. – Peter Drucker",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "You are never too old to set another goal or to dream a new dream. – C.S. Lewis",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "Do not wait to strike till the iron is hot; but make it hot by striking. – William Butler Yeats",
    "It does not matter how slowly you go as long as you do not stop. – Confucius",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "You miss 100% of the shots you don’t take. – Wayne Gretzky",
    "Hardships often prepare ordinary people for an extraordinary destiny. – C.S. Lewis",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. – Zig Ziglar",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. – Nelson Mandela",
    "Dream big and dare to fail. – Norman Vaughan",
    "Your time is limited, so don’t waste it living someone else’s life. – Steve Jobs"
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
