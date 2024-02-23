import random
import discord
from discord import Intents, Client, Message
from discord.ext import commands
import os, time
from random import choice
from dotenv import load_dotenv
from ttt import TTT



load_dotenv() # loads all the vars from the env file, used for bot token

# bot setup
intents: Intents = Intents(messages=True, guilds=True )
bot = commands.Bot(description="TTT Bot", command_prefix='!', intents=intents)

# bot logic 

@bot.event
async def on_ready():
    print(f'{bot.user} is up and ready for trouble')


@bot.event
async def on_message(message: Message):
    #debug line
    #print(message)
    

    if message.author.id != bot.user.id:

        #time_counter:int  = 0
        #ticket_counter:int = 0

        await bot.process_application_commands(message)
        #ticket_counter +=1
        
        
    
         
        # TODO replace 'binary' by TTType
        #   uniqueid: str -> create ticket id #
        #   messageid
        #
        #
        #obj = TTT(777, message.id, bot.user, 1000, 'binary', message.content)
        obi = TTT(message.id, bot.user.id, message.author.id, 0, 'alt', message.content)
         
        #obi.show_console_ticket(message, bot)
        #obj.show_channel_message(message, bot)
        time.sleep(obi.time)
        print('next step: delete previous message')


        # TODO correct this 
        new_messagelist = []
        if obi.type == 'binary':
            new_messagelist.append('01010101')
            new_messagelist.append('10101010') 
            new_messagelist.append('01101001')
        elif obi.type == 'robot':
            new_messagelist.append('beep')
            new_messagelist.append('boop')
            new_messagelist.append('buup')
        else:
            new_messagelist.append('~~~')
            new_messagelist.append('...')
            new_messagelist.append('---')
        #
        new_message : str = random.choice(new_messagelist)

        try:    
            await message.channel.send(f'{message.author.name} says {new_message}')
            #await obi.deletemessage()
            del obi

        except Exception as e:
            print(e)



bot.run(os.getenv('DISCORD_TOKEN'))