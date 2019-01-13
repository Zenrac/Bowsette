#!/usr/bin/env python3
import discord
import asyncio
import sys
from arcadia import Client
# You have to replace API_KEY to your arcadia token
arctoken = 'API_KEY'
arcadia = Client(token=arctoken)

# You have to replace BOT_TOKEN to your bot token
token = 'BOT_TOKEN'
prefix = 'b!'

class Bot(discord.Client):
    async def on_ready(self):
        await self.change_presence(activity=discord.Game(name=prefix+"help"))
        print(self.user.name+' connecté !')

    async def on_message(self, message):

        if message.author == self.user:
            return

        if message.content.startswith(prefix+'logout'):
            if message.author.id != 240508683455299584:
                return await message.channel.send('⚠ You\'re not my owner.')
            else:
                await message.channel.send('💤 I will go to sleep...')
                await sys.exit();

        if message.content.startswith(prefix+'arcadia'):
            if message.content.split(" ")[1]:
                try:
                    image = await arcadia.get_image(message.content.split(" ")[1], message.author.avatar_url_as(format='png'))
                    await message.channel.send(file=image)
                except:
                        await message.channel.send('❌ An error has occured.')
            else:
                    await message.channel.send('⚠ You must provide an endpoint.')

        elif message.content.startswith(prefix+'help'):
                Embed = discord.Embed(description='Here\'s my commands:', colour=0x36393f)
                Embed.set_author(name='Bowsette', icon_url=self.user.avatar_url)
                Embed.add_field(name='b!arcadia <endpoint>', value='Some endpoints: `angry`, `animeprotest`, `beautiful`, `blood`, `bloodhelp`, `bluely`, `blur`, `blurblack`, `blureen`, `blurey`, `blurple`, `bob`, `brazzers`, `codebabes`, `convinvert`, `convmatrix`, `convolute`, `cyanly`, `discordlogo`, `displace`, `distortion`, `gay`, `ghost`, `glitch`, `goodbye`, `grayscale`, `hitler`, `hypesquad`, `illuminati`, `implode`, `invert`, `jackolantern`, `link`, `loveship`, `magik`, `orangblur`, `orangly`, `pixelate`, `posterize`, `purply`, `rainbow`, `respect`, `sepia`, `shocked`, `snow`, `thisexample`, `thisfilm`, `time`, `tobecontinued`, `triggered`, `triggeredinvert`, `waifu`, `wanted`, `wasted`, `welcome`, `whoisthis`, `yelloblur`, `youporn`', inline=True)
                await message.channel.send(embed=Embed)

client = Bot()
client.run(token)
