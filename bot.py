from discord.ext import commands
import discord
import os

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = int(os.environ.get('CHANNEL_ID'))

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("git bot is ready")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

bot.run(BOT_TOKEN)