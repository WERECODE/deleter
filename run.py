import discord
from discord.ext import commands

with open('token.txt', 'r') as f:
    token = f.read().strip()


bot = commands.Bot(command_prefix='.', self_bot=True)

messages_to_delete = []

@bot.event
async def on_ready():
    print('Bot ready!')

@bot.event
async def on_message(message):
    global messages_to_delete
    # Check if the message content matches any of the phrases in the list
    if any(phrase in message.content for phrase in messages_to_delete):
        await message.delete()

    await bot.process_commands(message)


@bot.command()
async def set(ctx, *args):
    global messages_to_delete
    messages_to_delete = list(args)  # Set the list of messages to delete based on user input
    await ctx.message.delete()


@bot.command()
async def clear(ctx):
    global messages_to_delete
    messages_to_delete = []  # Clear the list of messages to delete
    await ctx.message.delete()

bot.run(token)