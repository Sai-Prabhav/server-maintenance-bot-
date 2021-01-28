import discord
import random
import os
import json
from lib import *
from discord.ext import commands
from keep_alive import keep_alive
import datetime

timer = datetime.datetime.now()
client = commands.Bot(command_prefix='^')


data = load()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print(load()['score'])


@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author == client.user:
        return

    # if  :
    #     await message.channel.purge(limit=1)
    #     await message.channel.send('dont type such words')
    if message.content.startswith('bots are fun'):
        await message.channel.send('true thats so i am hear!')


@client.event
async def on_member_join(member):
    print(f'{member} has joined')


@client.event
async def on_member_remove(member):
    print(f'{member} has left')



@client.command()
async def answer(ctx, *, ans):

    if not(data["answer"][timer.strftime("%x")]):
        data["answer"][timer.strftime("%x")] = {}
    data["answer"][timer.strftime("%x")][name(ctx.author)] = ans
    save(data)



@client.command()
async def inbot(ctx, ):
    await ctx.send('plz use your command in #bots its prohibited to use it here')


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
async def score(ctx, man: discord.Member):
    if not (man):
        man = ctx.author
    if data['score'].get(name(man)):
        await ctx.send(data['score'][name(man)])
    else:
        data["score"][name(man)] = 100
        await ctx.send(data["score"][name(man)])


@client.command()
async def scores(ctx):
    matches = data['score']
    for x in matches:

        await ctx.send(f"{x} --> {matches[x]}")
    save(data)


@client.command()
@commands.has_any_role("Admin", "Owner")
async def warn(ctx, man: discord.Member):
    await ctx.send(
        f"you will be kicked if you repeat this once more <@{man.id}> ")
    if data['score'].get(name(man)):

        data['score'][name(man)] -= 5

        if data['score'][name(man)] < 25:
            pass

    else:
        data['score'][name(man)] = 100
    save(data)
    await ctx.send(data['score'][name(man)])


@client.command()
@commands.has_any_role("Admin", "Owner")
async def clear(ctx, x=5):
    await ctx.channel.purge(limit=x)

@client.command()
@commands.has_any_role("Admin", "Owner")
async def givescore(ctx, man: discord.Member):

    if data['score'][name(man)]:

        data['score'][name(man)] += 10
    else:
        data['score'][name(man)] = 100
    save(data)
    await ctx.send(data['score'][name(man)])


@client.command()
@commands.has_any_role("Admin", "Owner")
async def mute(ctx, member: discord.Member):
    user = ctx.guild.roles

    await member.add_roles(user[1])


@client.command()
@commands.has_any_role("Admin", "Owner")
async def unmute(ctx, member: discord.Member):
    user = ctx.guild.roles
    await member.remove_roles(user[1])


@client.command()
async def rules(ctx):
    await ctx.send(
        rules())


keep_alive()
client.run(os.getenv('TOKEN'))
