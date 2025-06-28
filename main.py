import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
BOTTOKEN = os.getenv("BOTTOKEN")

# Verificar se o token está configurado
if not BOTTOKEN:
    print("ERRO: Token do bot não encontrado!")
    print("Por favor, crie um arquivo .env na raiz do projeto com o seguinte conteúdo:")
    print("BOTTOKEN=SEU_TOKEN_AQUI")
    print("Substitua 'SEU_TOKEN_AQUI' pelo token real do seu bot Discord.")
    exit(1)

# Debug: mostrar se o token está sendo carregado (ocultando parte do token por segurança)
if BOTTOKEN:
    token_preview = BOTTOKEN[:10] + "..." if len(BOTTOKEN) > 10 else "Token muito curto"
    print(f"Token carregado: {token_preview}")
    print(f"Comprimento do token: {len(BOTTOKEN)}")

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

# Tratamento de erro para problemas de autenticação
try:
    bot.run(BOTTOKEN)
except nextcord.errors.LoginFailure as e:
    print("ERRO DE AUTENTICAÇÃO:")
    print("O token do bot é inválido ou expirou.")
    print("Verifique se:")
    print("1. O token está correto no Railway")
    print("2. O bot ainda existe no Portal de Desenvolvedores")
    print("3. O token não foi resetado")
    print(f"Erro detalhado: {e}")
    exit(1)
except nextcord.errors.Unauthorized as e:
    print("ERRO DE AUTORIZAÇÃO:")
    print("O token fornecido não tem permissões adequadas.")
    print("Verifique se o token é válido e pertence a um bot.")
    print(f"Erro detalhado: {e}")
    exit(1)
except Exception as e:
    print(f"ERRO INESPERADO: {e}")
    exit(1)
