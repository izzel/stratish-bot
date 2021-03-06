import discord
import time
from os import system

with open("token", "r") as f:
	TOKEN = f.read().rstrip()

client = discord.Client();


###############################################################################


@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	await client.change_presence(game=discord.Game(name='/stratish [word]'))
	



@client.event
async def on_message(M):
	print("#"+M.channel.name,"<"+str(M.author)+">", M.content)
	
	if(M.content.startswith('/stratish')):
		await client.send_typing(M.channel)
		words=M.content[10:]
		ut = time.strftime("%s")
		tmpfile = "tmp/img-"+str(ut)+".png"
		command = "writer/writer '%s' >%s" % (words, tmpfile)
		print("$", command)
		system("touch "+tmpfile)
		system(command)
		await client.send_file(M.channel, tmpfile)
	

client.run(TOKEN);
