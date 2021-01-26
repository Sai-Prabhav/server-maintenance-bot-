import discord
import random
from discord.ext import commands
from keep_alive import keep_alive
from replit import db

keys = db.keys()
client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author == client.user:
        return
    if 'fuck' in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send('dont type suck words')
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('bots are fun'):
        await message.channel.send('true thats so i am hear!')


@client.event
async def on_member_join(member):
    print(f'{member} has joined')


@client.event
async def on_member_remove(member):
    print(f'{member} has left')


@client.command()
@commands.has_any_role("Admin", "Medium Cheese")
async def clear(ctx, x=5):
    await ctx.channel.purge(limit=x)


@client.command()
async def hi(ctx):
    await ctx.send(f"hi <@{ctx.author.id}>")


@client.command()
async def ping(ctx):
    await ctx.send(f"ping is {round(client.latency*1000)}ms")


@client.command()
async def toss(ctx):
    await ctx.send(random.choice(['heads', 'tails']))


@client.command()
async def keys(ctx):
    await ctx.send(db.keys())


@client.command()
async def score(ctx, man: discord.Member):
    if not(man):
        man = ctx.author
    if db.get(str(man.name)+"_score"):
        await ctx.send(db.get(str(man.name)+"_score"))
    else:
        db[str(man.name)+"_score"] = 100
        await ctx.send(db.get(str(man.name)+"_score"))


@client.command()
@commands.has_any_role("Admin", "Medium Cheese")
async def warn(ctx, man: discord.Member):
    await ctx.send(
        f"you will be kicked if you repeat this once more <@{man.id}> ")
    if db.get(str(man.name)+"_score"):
        db[str(man.name)+"_score"] -= 5
        if  db[str(man.name)+"_score"]<25:
            pass
    else:
        db[str(man.name)+"_score"] = 100

    await ctx.send(db.get(str(man.name)+"_score"))


@client.command()
async def rules(ctx):
    await ctx.send(
        '''#1 - Be nice to one another, respect each other's opinions.
#2 - Dont send hateful messages.
#3 - No nsfw or inappropriate messages should be sent.
#4 - If anyone encounters any issue, Ping the @Admin they will address the issue.
#5 - suggestions can be given in #suggestions 
#6 - No spamming please or pinging of @everyone 
#7 - No racist or homophobic messages, photos ,videos etc
#8 - This is an English speaking server so speak in English to the best of your ability

People who do not abide with these rules will be banned or muted from the server
Have a good time at this server!''')

keep_alive()
client.run('ODAzMTAzMDAyMjYwMTQ0MTU4.YA459A.2LonZJ3g_At_oUa9BTxLw6YJkiA')
