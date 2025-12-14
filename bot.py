import argparse
import random

import discord
from discord.ext import commands

from game.challenge_randomiser import ChallengeRandomiser


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--sync", action="store_true")
args = vars(parser.parse_args())


randomiser = ChallengeRandomiser()

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())


@bot.event
async def on_ready():
    if args["sync"]:

        # TODO remove once this is no longer needed
        for guild in bot.guilds:
            bot.tree.clear_commands(guild=guild, type=None)
            await bot.tree.sync(guild=guild)

        await bot.tree.sync()


@bot.tree.command(
    name="add",
    description="Add a random challenge to the list.",
)
async def challenges(interaction: discord.Interaction):
    randomiser.add()
    await interaction.response.send_message(randomiser.challenges())


@bot.tree.command(
    name="challenges",
    description="Show all challenges in the list.",
)
async def challenges(interaction: discord.Interaction):
    await interaction.response.send_message(randomiser.challenges())


@bot.tree.command(
    name="random",
    description="Generate a random number between 1 and n.",
)
async def random_(interaction: discord.Interaction, n: str):
    if n.isdigit():
        await interaction.response.send_message(f"{random.randint(1, int(n))}")
    else:
        await interaction.response.send_message(f"n must be integer")


@bot.tree.command(
    name="reset",
    description="Remove all challenges from the list.",
)
async def reset(interaction: discord.Interaction):
    randomiser.reset()
    await interaction.response.send_message("removed all challenges")


@bot.tree.command(
    name="quit",
    description="Stop running the bot.",
)
async def quit(interaction: discord.Interaction):
    await interaction.response.send_message("quitting")
    await bot.close()


with open("token.txt") as file:
    TOKEN = file.read().strip()

bot.run(TOKEN)
