import nextcord
from nextcord.ext import commands
import os
from apikeys import BOTTOKEN

intents = nextcord.Intents.all()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix = "?", intents = intents)

def import_cogs():
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"Cog carregada: {filename}")

@bot.event
async def on_ready():   
    import_cogs()
    await bot.sync_all_application_commands()
    print("Todos os comandos foram sincronizados.")
    print(f"{bot.user.name} foi iniciado.")

bot.run(BOTTOKEN)
