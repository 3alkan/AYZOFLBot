import os
import traceback
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
token = os.getenv("AYZOFLBot_Token")

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)

tree = bot.tree


@bot.event
async def on_ready():
    await tree.sync()
    print('Commands synchronized globally.')
    print(f"Logged in as {bot.user}")
    for guild in bot.guilds:
        print(f"Connected to guild: {guild.name} (ID: {guild.id})")

@bot.event
async def on_command_error(ctx, error):
    print(f"An error occurred: {error}")
    await ctx.send("An error occurred while processing the command.")

@bot.event
async def on_app_command_completion(interaction: discord.Interaction, command: discord.app_commands.Command):
    print(f"Command '{command.name}' completed by user {interaction.user.name} in guild {interaction.guild.name}.")

@tree.command(name="help", description="Displays help information.")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message("this is help command")

bot.run(token)
