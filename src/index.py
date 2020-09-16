import discord
from discord.ext import commands

import datetime
import random


bot=commands.Bot(command_prefix='!',descripción='este es un bot de pruebas')

#Comando !ping
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

#Comando !sum
@bot.command()
async def sum(ctx,one:int,two:int):
    await ctx.send(one+two)

#Comando !stats
@bot.command()
async def stat(ctx):
    embed=discord.Embed(title=f"{ctx.guild.name}", description="Mensaje embebido.", timestamp=datetime.datetime.utcnow(), 
    color=discord.Color.green())
    embed.add_field(name="Server creado el ", value=f"{ctx.guild.created_at}") #la f le da el formato de salida que se desea
    embed.add_field(name="Creador del server ", value=f"{ctx.guild.owner}")
    embed.add_field(name="Región del server ", value=f"{ctx.guild.region}")
    embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/644969205876551680/T5g3D12v_400x400.png")
    await ctx.send(embed=embed)

#adivina el número random
@bot.command()
async def adivina(ctx, num:int):
    guess=random.randint(1,10)
    if num==guess:
      await ctx.send('Adivinaste! :partying_face: ')
      await ctx.send(guess)
    else:
      await ctx.send('Sigue intentando :stuck_out_tongue: ')
      await ctx.send(guess)

@bot.command()
async def hola(ctx):
    saludos=['hola','holiwi','¿qué onda?', 'aloha', 'holi boli'] #creamos la variable que contendrá la lista de mensajes posibles
    await ctx.send(random.choice(saludos))

#Events
@bot.event
async def on_ready():
    print ('Es bot ya está listo')

bot.run('')