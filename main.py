import discord

client = discord.Client()

TOKEN = ""

@client.event
async def on_ready():
	print(f"Logged in as {client}")

@client.event
async def on_message(message):
	# If the message is from ourselves, do nothing.
	if message.author == client.user:
		return
	
	print(message)

client.run(TOKEN)
