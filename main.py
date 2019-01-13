#!/usr/bin/env python3
import discord
import asyncio
import sys

from arcadia import Client
from arcadia.errors import Forbidden, InvalidEndPoint

arctoken = 'API_KEY'  # You have to replace API_KEY to your arcadia token
arcadia = Client(token=arctoken)

token = 'BOT_TOKEN'  # You have to replace BOT_TOKEN to your bot token
prefix = 'b!'  # Custom prefix
owner_id = 'OWNER_ID'  # You have to replace OWNER_ID to your ID


class Bot(discord.Client):
    """Bot class"""

    async def on_ready(self):
        game = discord.Game(name='{}help'.format(prefix))
        await self.change_presence(activity=game)
        print('Connected as: {} ({})'.format(str(self.user), str(self.user.id)))
        print('Owner: {}'.format(owner_id))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if not message.content.startswith(prefix):
            return

        command = message.content.lower().strip()[len(prefix):]  # Case insensitive

        if command.startswith('logout'):
            if message.author.id != int(owner_id):
                await message.channel.send('⚠ You\'re not my owner.')
            else:
                await message.channel.send('💤 I will go to sleep...')
                await sys.exit()

        elif command.startswith('arcadia'):
            if len(message.content.split(' ')) < 2:
                return await message.channel.send('⚠ You must provide an endpoint.')

            endpoint = message.content.split(' ')[1]  # Only works if endpoints are in one word

            try:
                image = await arcadia.get_image(endpoint, message.author.avatar_url_as(format='png'))
                await message.channel.send(file=image)
            except Forbidden:
                await message.channel.send('❌ You are not allowed to access this endpoint.')
            except InvalidEndPoint:
                await message.channel.send('❌ This endpoint doesn\'t exist!')

        elif command.startswith('help'):
            embed = discord.Embed(description='Here\'s my commands:', colour=0x36393f)
            embed.set_author(name=self.user.name, icon_url=self.user.avatar_url)
            endpoints = '`{}`'.format('`, `'.join(arcadia.endpoints))
            embed.add_field(name='{}arcadia <endpoint>'.format(prefix), value=endpoints)
            embed.add_field(name='{}help'.format(prefix), value='Displays this message', inline=False)
            if message.author.id == int(owner_id):
                embed.add_field(name='{}logout'.format(prefix), value='To ask me to disconnect myself', inline=False)
            await message.channel.send(embed=embed)


client = Bot()
client.run(token)
