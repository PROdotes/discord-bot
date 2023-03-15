import discord

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
        await message.channel.send('Bleat!')


with open("C:\\Users\\prodo\\PycharmProjects\\discord\\key.txt") as file:
    TOKEN = file.read().strip()
    print(TOKEN)
    client.run(TOKEN)
