import os
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command(name='any', help='Responds with '' quotes from '')
async def 'name'(ctx):
    quotes = ['array of quotes/text file/etc'
    ]

    response = random.choice(quotes)
    await ctx.send(response)

bot.run(token)
