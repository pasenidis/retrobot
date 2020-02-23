import discord
from discord.ext import commands
import random

token  = 'Null' # DO NOT ENTER! CREATE A FILE WITH YOUR CREDENTIALS AND NEVER SHARE IT!
client = commands.Bot(command_prefix = 'r!')

f = open('credentials.txt', 'r')
if f.mode == 'r':
    token = f.read()


@client.event # On startup
async def on_ready():
    # print("Hello, I am Retro! I am a slave, I can do whatever His Majesty User wants.")
    print("RetroBot is up and ready!")

@client.event # When a member joins the server
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event # When a member lefts the server
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.command(aliases=['latency', 'ms'])
async def ping(ctx):
    await ctx.send(f'Pong! Latency: **{round(client.latency * 1000)}ms**')

@client.command(aliases=['8ball', 'eightball'])
async def _8ball(ctx, *, question):
    responses = [    
        'It is certain.',
        'It is decidedly so.',
        'Without a doubt.',
        'Yes - definitely.',
        'You may rely on it.',
        'As I see it, yes.',
        'Most likely.',
        'Outlook good.',
        'Yes.',
        'Signs point to yes.',
        'Reply hazy, try again.',
        'Ask again later.',
        'Better not tell you now.',
        "Cannot predict now.",
        'Concentrate and ask again.',
        "Don't count on it.",
        'My reply is no.',
        'My sources say no.',
        'Outlook not so good.',
        'Very doubtful.']
    await ctx.send(f'> {question}' + f'\n**{random.choice(responses)}**')

client.run(token)