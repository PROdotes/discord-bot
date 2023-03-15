import discord
import json

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# Load the user dictionary from file
try:
    with open("users.txt", "r") as file:
        users = json.load(file)
except FileNotFoundError:
    users = {}


# report when loaded
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


# listen to messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # if someone mentions goat, tell them how many times they did it and save the new vaule
    if "goat" in message.content.lower():
        author_id = str(message.author.id)
        users[author_id] = users.get(author_id, 0) + 1
        await message.channel.send(f"Bleat! You bleated {users[author_id]} times.")
        with open("users.txt", "w") as file:
            json.dump(users, file)


# read the token from the key file, so it's not in the git
with open("key.txt") as file:
    TOKEN = file.read().strip()
    print(f'Your token is: {TOKEN}')
    client.run(TOKEN)
