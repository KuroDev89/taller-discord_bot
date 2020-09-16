#Verificar versión de python
python --version

# Instalar pip
  #Descargar instalador
   curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

  #Ejecutar instalador
   python get-pip.py

#Instalar pipenv: herramienta que permite crear entorno virtual
pip3 install pipenv #si tienes más de una versión de python coloca el número correspondiente, sino solo con 'pip install pipenv' será suficiente
  #en el file pipfile se listan las dependencias/módulos que requiere nuestro proyecto

#Crear entorno virtual
pipenv shell

#instalar biblioteca de discord
pipenv install discord.py

#crear una carpeta (opcional) con un archivo index.py
src

#importar la biblioteca de discord y algunas clases como commands
  import discord
  from discord.ext import commands  

  #inicializa el bot
  bot=commands.Bot(command_prefix='',descripción='')

  #usamos el decorador @bot.command() para crear comandos
  @bot.command()
  async def ping(ctx): #ctx le dirá a python que trabajaremos con la biblioteca de discord.py
    await ctx.send('pong') #async y await para señalar la co-rutina, pues estos comandos no se ejecutan de inmediato

  #ingresar token para que el bot responda a los comandos
  bot.run('token') #registrar app en discord, vamos a discord dev
    #tras crear la app ir a la pestaña bot (lado izq) y darle a añadir bot (add bot) y le damos permisos de adm
    #copiamos el token (mantenlo en secreto) y lo pegamos en nuestro código
    #creamos un servidor de discord y agregamos el bot en la pestaña Auth y seleccionamos registrar bot
    #abrimos la url y seleccionamos a qué server lo vamos a agregar
  
  #Generamos un evento para que nos avise cuando el bot se conecte
  @bot.event
  async def on_ready():
      print ('Es bot ya está listo')

  #ejecutamos nuestro archivo
  python src/index.py

  #probamos el comando !ping en discord

  #pausamos el bot con Crtl + C

  #Hacer que el bot sume 2 números (argumentos) enteros
  @bot.command()
  async def sum(ctx,one:int,two:int): #especificar el tipo de dato int, para que realice la suma
    await ctx.send(one+two)

#importar biblioteca datetime
import datetime

#como mostrar estadísticas del server
@bot.command()
async def stat(ctx):
    embed=discord.Embed(title=f"{ctx.guild.name}", description="Mensaje embebido.", timestamp=datetime.datetime.utcnow(), 
    color=discord.Color.blue())#la f le da el formato de salida que se desea sin generar conflicto
    embed.add_field(name="Server creado el ", value=f"{ctx.guild.created_at}") #fecha de creación del server
    embed.add_field(name="Creador del server ", value=f"{ctx.guild.owner}") #nombre del creador del server
    embed.add_field(name="Región del server ", value=f"{ctx.guild.region}")
    embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/644969205876551680/T5g3D12v_400x400.png") #imagen del server
    await ctx.send(embed=embed)

@bot.command()
async def info(ctx):
  embed=discord.Embed(tittle=f"{ctx.guild.name}", 
  description="Mensaje enriquecido", timestamp=datetime.uctnow()) #esta es solo la variable,aquí usamos la variable
await ctx.send(embed=embed) #enviamos un embed que tiene como valor la variable embed

#importamos la libreria
import random

#saludo random
@bot.command()
async def hola(ctx):
    saludos=['hola','holiwi','¿qué onda?', 'aloha', 'holi boli'] #creamos la variable que contendrá la lista de mensajes posibles
    await ctx.send(random.choice(saludos))

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