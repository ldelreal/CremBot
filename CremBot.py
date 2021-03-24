import os
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command(name='stick', help='Responds with Stick quotes from Stromlight Archive')
async def stick(ctx):
    i_am_stick_quotes = [
        (
            'Why don’t you become fire instead? :fire:'
            '\n'
            '\nI am a stick.:wood:'
        ),
        (
            'You want to burn? :fire:'
            '\n'
            '\nI am a stick.:wood:'
        ),
        (
            'Think of how much fun it would be? :tada:'
            '\n'
            '\nI am a stick.:wood:'
        ),
        'I am a stick.:wood:'
    ]

    response = random.choice(i_am_stick_quotes)
    await ctx.send(response)


@bot.command(name='pattern', help='Responds with Pattern quotes from Stromlight Archive')
async def pattern(ctx):
    pattern_quotes = [
        (
            'Inappropriate?'
            '\nSuch as...'
            '\nDividing by zero? :zero:'
        ),
        (
            'No mating.'
            '\n'
            '\nNO MATING.'
            '\n'
            '\nNO MATING!'

        ),
        (
            'You were talking about mating! '
            '\n'
            '\nI’m to make sure you don’t accidentally mate.'
        ),
        'Terrible destruction to eat!:meat_on_bone:',
        'Yes, yes. Mmmm.'
    ]

    response = random.choice(pattern_quotes)
    await ctx.send(response)

bot.run(token)
