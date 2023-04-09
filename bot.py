from discord.ext import commands
from discord.ext.commands import UserConverter
import discord
import gspread
import asyncio
from botfunctions import *

BOT_TOKEN = ""

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("mademoiselle is ready")
    
@bot.command()
async def ping(ctx):
    await ctx.send("fufu")

@bot.command()
# you can call this in other functions if you need to send a dm
# works with the username#0000 format as a string
async def dm(ctx, user: discord.User, message):
    # convert it to a user for Realsies bc it wont otherwise for some reason
    converter = UserConverter()
    user = await converter.convert(ctx, user)
    await user.send(message)
    
@bot.command()
async def contact(ctx, sheet, message, status, worksheet='Sheet1'):
    ws = getSheet(sheet, worksheet)
    # returns a list that contains dictionaries for each claimer
    # keys are the headers of every column
    records = getRecords(ws)
    
    for i in records:
        if i['status'] == status:
            # isolating user to dm
            user = i['discord']
            # this does the same thing that f"{}" would do except its for variables. i think
            # you can use any variable that is a column in your spreadsheet
            # e.g., discord, name, cost, quantity, etc.
            namespace = i
            msg = message.format(**namespace)

            try:
                await dm(ctx, user, msg)
            except:
                await ctx.send(f"Unable to DM {user}.")
    await ctx.send("Task completed!")
            
@bot.command()
async def paid(ctx, split, user):
    try:
        # this uses nicknames
        sheet = getNickname(split)
        ws = getSheet(sheet)
        # this is kind of suck im ngl
        row = ws.find(user)
        col = ws.find('status')
        # update their status
        ws.update_cell(row.row, col.col, 'paid')
        await ctx.send("Thank you! Your GOM has been notified. If they need to follow up with you, they will contact you directly.\nIf you have any questions or concerns, you can do `!q (question here)`, or message `username#0000` directly.")
    except:
        await ctx.send("I wasn't able to complete your request. If you've changed your username recently, try using your old one. If you're still having trouble, you can use `!q (question here)` and I'll relay the message, or message `username#0000` directly.")
@bot.command()
async def q(ctx, *, message):
    # change to your username#0000
    user = "username#0000"
    msg = f"from {ctx.author}: {message}"
    try:
        await dm(ctx, user, msg)
        await ctx.send("Your question has been relayed, your GOM will be contacting you ASAP. Thank you for your patience!")
    except:
        await ctx.send("There was an error on my end and I wasn't able to relay your question. Please contact `username#0000` directly.")
        
bot.run(BOT_TOKEN)