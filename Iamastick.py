import os
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command(name='stick', help='Responds with stick passage from Stromlight Archive')
async def stick(ctx):
    i_am_stick_quotes = [
        (
            'Why don’t you become fire instead? :fire:'
            
            '\n I am a stick.:wood:'
        ),
        (
            'You want to burn? :fire:'
            
            '\n I am a stick.:wood:'
        ),
        (
            'Think of how much fun it would be? :tada:'

            '\n I am a stick.:wood:'
        ),
        'I am a stick.:wood:'
    ]

    response = random.choice(i_am_stick_quotes)
    await ctx.send(response)

bot.run(token)
