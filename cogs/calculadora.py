from nextcord.ext import commands
from nextcord import Interaction, SelectOption, Embed, ButtonStyle
from nextcord.ui import View, Select, Button

from cogs.modais.robuxreais import RobuxParaReais
from cogs.modais.reaisrobux import ReaisParaRobux
from cogs.modais.giftreais import GiftParaReais

# selecionar categorias

class CalcSelect(Select):
    def __init__(self, bot):
        options = (
            SelectOption(label = "Robux para Reais", value = "robux"),
            SelectOption(label = "Reais para Robux", value = "reais"),
            SelectOption(label = "Gift para Reais", value = "gift")
        )
        super().__init__(
            placeholder = "Selecione o que você deseja calcular.", 
            min_values = 1, 
            max_values = 1, 
            options = options)
        self.bot = bot
    
    async def callback(self, interaction: Interaction):
        categoria = self.values[0]

        if categoria == "robux":
           await interaction.response.send_modal(RobuxParaReais(self.bot))
        
        elif categoria == "reais":
            await interaction.response.send_modal(ReaisParaRobux(self.bot))

        else:
            await interaction.response.send_modal(GiftParaReais(self.bot))

# view do select

class CalcSelectView(View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.add_item(CalcSelect(bot))

# embed principal

class Calculadora(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command(name = "calculadora")
    async def calculadora(self, ctx: commands.Context):
        await ctx.message.delete()

        embed = Embed(
            description = ("# <:e_cbxarrow:1378148186249494669> Painel de Valores \n"
            "\n"
            "> Olá! Bem-vindo(a) ao nosso __Painel de Valores__. Selecione uma das opções abaixo para ver o valor correspondente ao item desejado. \n"
            "\n"
            "Não sabe como comprar? [clique aqui](https://discord.com/channels/1187947032183308389/1345258994759110730)."
            ), 
            color = 0x54AB4B,
        )

        embed.set_image(url = "https://media.discordapp.net/attachments/1359230400005935136/1378115111587151882/CBX_Tabela_Robux.gif?ex=6845f936&is=6844a7b6&hm=8cc4dfba1f4d91bb07fe69d6f57e861b1e4d391653bdbc7f588f91de77326bef&=&width=1000&height=563")

        await ctx.send(embed = embed, view = CalcSelectView(self.bot))

def setup(bot):
    bot.add_cog(Calculadora(bot))
