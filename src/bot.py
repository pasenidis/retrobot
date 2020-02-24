import discord
from discord.ext import commands
import random, asyncio

token  = 'Null' # DO NOT ENTER! CREATE A FILE WITH YOUR CREDENTIALS AND NEVER SHARE IT!
client = commands.Bot(command_prefix = 'r!') # CHANGE THE PREFIX HERE

f = open('credentials.txt', 'r')
if f.mode == 'r':
    token = f.read()

@client.event # On startup
async def on_ready():
    # print("Hello, I am Retro! I am a slave, I can do whatever His Majesty User wants.")
    print("RetroBot is up and ready!")
    await client.change_presence(activity=discord.Game(name='r!help'))

@client.event # When a member joins the server
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event # When a member lefts the server
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.command() 
async def kick(ctx, member : discord.Member, * , reason=None): 
    await member.kick(reason=reason)
    await ctx.send(f':x: {str(member)} was kicked because **{reason}**')    

@client.command() 
async def ban(ctx, member : discord.Member, * , reason=None): 
    await member.ban(reason=reason)
    await ctx.send(f':x: {str(member)} was banned because **{reason}**')
    
@client.command() 
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f':x: {user.name} was forgiven!')

@client.command()
async def announce(ctx, id, *, announcement):
    channel = client.get_channel(int(id))
    await channel.send(f'> {announcement} @everyone')

# @client.command()
# async def setstatus(ctx, status = 'Null'):
#     await client.change_presence(activity=discord.Game(name=str(status)))

@client.command(aliases=['purge'])
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit = amount)
    await asyncio.sleep(1)
    await ctx.send(f':wastebasket: Cleared the chat as {ctx.author.mention} requested!')

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