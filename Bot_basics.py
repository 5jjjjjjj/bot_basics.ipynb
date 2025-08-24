import os
import discord
from discord.ext import commands  # Corrected import
from dotenv import load_dotenv

# Load environment variables from .env file
os.path.dotenv = '.env'
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Define bot intents
intents = discord.Intents.default()
intents.message_content = True  # Enable the message_content intent

# Create a bot instance
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Basic ping command
@bot.command('ping')
async def ping(ctx):
    """Responds with 'Pong!' and latency."""
    latency = bot.latency
    await ctx.send(f'Pong! Latency: {latency*1000:.2f} ms')

# Command: Basic hello command
@bot.command(name='hello')
async def hello(ctx):
    """Responds with a greeting."""
    await ctx.send('Hello!')

@bot.command(name='gosleep')
async def gosleep(ctx):    
    """Disconnects the bot from the server."""
    await ctx.send("Goodnight!")
    await bot.close()


# Run the bot (use token from .env, not hardcoded)
bot.run(TOKEN)
