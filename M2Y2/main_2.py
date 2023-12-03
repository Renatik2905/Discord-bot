import discord
import random
from discord.ext import commands
import os
import requests
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Бот {bot.user} запущен!')

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command()
async def ecology(ctx):
    egology_name = random.choice(os.listdir("Egology"))
    with open(f'Egology/{egology_name}', 'rb') as f:
        
        picture = discord.File(f)
   
    await ctx.send(file=picture)



@bot.command()
async def news(ctx): 
     eco = "https://ecoportal.su/news/top.html" 
   
     await ctx.send(eco)   

@bot.command()
async def Save_our_planet(ctx): 
     Save = "https://turclub-pik.ru/blog/chto-ya-mogu-sdelat-dlya-ehkologii-30-sposobov/"
     Answer = ("lets see how to save our planet!")
     await ctx.send(Save)
     await ctx.send(Answer)



bot.run('MTE0NzgyOTYwMTY3MDgxMTcyOA.GSGwB5.v7q4W7kW113DDykXdCabCmp9vWMhYwY_DyzBO0')