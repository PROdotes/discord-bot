import discord
from discord.ext import commands
from discord.ui import Button, View
import json

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())
GUILD = discord.Object(id=164443857163911168)


# Load the user dictionary from file
try:
    with open("users.txt", "r") as file:
        users = json.load(file)
except FileNotFoundError:
    users = {}


@bot.event
async def on_ready():
    print(f'Bot logged in as {bot.user}')
    try:
        synced = await bot.tree.sync(guild=GUILD)
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)


@bot.tree.command(name='goat', description='fancy goat stuff', guild=GUILD)
async def goat(interaction: discord.Interaction):
    response = f"Congrats on sending your command, {interaction.user.mention}!"
    view = View()
    button = Button(label='Button!')
    async def button_reaction(interaction):
        id = str(interaction.user.mention)[1:]
        users[id] = users.get(id,0)+1
        with open("users.txt", "w") as file:
            json.dump(users, file)
        await interaction.response.edit_message(content= f'you have clicked the button {users[id]} times.', view=None)
    button.callback = button_reaction
    view.add_item(button)
    await interaction.response.send_message(response, ephemeral=True, view=view)


# read the token from the key file, so it's not in the git
with open("key.txt") as file:
    TOKEN = file.read().strip()
    print(f'Your token is: {TOKEN}')
    bot.run(TOKEN)

