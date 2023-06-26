import os
import base64
import pyperclip
import discord
import random
import re
import time
from discord.ext import commands
from colorama import Fore
from tqdm import tqdm, trange
from time import sleep
from os import system


def clear(): return os.system('cls') if os.name == 'nt' else os.system('clear')
os.system("mode con cols=60 lines=20")
system("title " + "AFK COUNTER")


clear()
token = input('Welcome User! Please Enter your Discord Token Here: ')


class counter(discord.Client):
    async def on_ready(self):

        clear()
        print(f""" \u001b[31m
╔═╗╔═╗╦╔═  ╔═╗╔═╗╦ ╦╔╗╔╔╦╗╔═╗╦═╗
╠═╣╠╣ ╠╩╗  ║  ║ ║║ ║║║║ ║ ║╣ ╠╦╝
╩ ╩╚  ╩ ╩  ╚═╝╚═╝╚═╝╝╚╝ ╩ ╚═╝╩╚═
-------------------------------------
WELCOME {self.user}
               """)

    async def on_message(self, x):
        regex = re.findall(r'<@!?([0-9]+)>', x.content)
        if regex and 'afk' in x.content.lower() and x.author == self.user:
            for i in range(2, 100001):
                await x.channel.send(i)
                if i > 29:
                  time.sleep(1.7)


client = counter()
client.run(token, bot=False)
