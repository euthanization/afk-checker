import os
import base64
import pyperclip
import discord
import random
import re
from discord.ext import commands
from colorama import Fore
from tqdm import tqdm, trange
from time import sleep


def clear(): return os.system('cls') if os.name == 'nt' else os.system('clear')
os.system("mode con cols=60 lines=20")


clear()
token = input('Input Token Here: ')


class counter(discord.Client):
    async def on_ready(self):
        os.system(
            f'title [AFK Checker] | Connected As: {self.user}')

        clear()
        print(f""" \u001b[31m
╔═╗╔═╗╦╔═  ╔═╗╔═╗╦ ╦╔╗╔╔╦╗╔═╗╦═╗
╠═╣╠╣ ╠╩╗  ║  ║ ║║ ║║║║ ║ ║╣ ╠╦╝
╩ ╩╚  ╩ ╩  ╚═╝╚═╝╚═╝╝╚╝ ╩ ╚═╝╩╚═
-------------------------------------
               """)

    async def on_message(self, x):
        regex = re.findall(r'<@!?([0-9]+)>', x.content)
        if regex and 'start' in x.content.lower() and x.author == self.user:
            for i in range(2, 100001):
                time.sleep(3600)
                await x.channel.send(i)



client = counter()
client.run(token, bot=False)
