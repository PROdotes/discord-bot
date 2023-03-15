import discord
import json

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print(message)
    print(message.channel.permissions_for(message.author))
    print("#"+message.content+"#")

    if message.author == client.user:
        return

    if "goat" in message.content.lower():
        author_id = str(message.author.id)
        users[author_id] = users.get(author_id, 0) + 1
        with open("users.txt", "w") as f:
            json.dump(users, f)
        await message.channel.send('Bleat! you bleated ' + str(users[author_id]) + ' times')

# Load the users dictionary from file
try:
    with open("users.txt") as f:
        users = json.load(f)
except FileNotFoundError:
    users = {}

with open("C:\\Users\\prodo\\PycharmProjects\\discord\\key.txt") as file:
    TOKEN = file.read().strip()
    print(TOKEN)
    client.run(TOKEN)
