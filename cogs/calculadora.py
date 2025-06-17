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
            SelectOption(label = "Robux", value = "robux", emoji = "<:e_robux:1378175850113007727>"),
            SelectOption(label = "Gift", value = "gift", emoji = "<:e_cbxstar:1378175878327959675>")
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
            embed = Embed(
                description = (
                    "# <:e_cbxarrow:1378148186249494669> Calculadora de Robux \n"
                    "> Para calcular, selecione uma das opções abaixo: \n"
                    "\n"
                    "<:e_robux:1378175850113007727> **Robux para reais:** \n"
                    "> Calcula a quantidade de robux desejada em reais. \n"
                    "\n"
                    "<:e_robux:1378175850113007727> **Reais para robux:** \n"
                    "> Calcula a quantia de reais desejada em robux."
                    ),
                    color = 0x54AB4B
                )
            
            view = View(timeout = None)

            botao1 = Button(label = "Robux para Reais", style = ButtonStyle.green)
            botao2 = Button(label = "Reais para Robux", style = ButtonStyle.green)

            async def callback1(interaction: Interaction):
                await interaction.response.send_modal(RobuxParaReais(self.bot))

            async def callback2(interaction: Interaction):
                await interaction.response.send_modal(ReaisParaRobux(self.bot))

            botao1.callback = callback1
            botao2.callback = callback2

            view.add_item(botao1)
            view.add_item(botao2)

        else:
            embed = Embed(
                description = ("# <:e_cbxarrow:1378148186249494669> Calculadora de Gift \n"
                    "> Para calcular, selecione a opção abaixo: \n"
                    "\n"
                    "<:e_cbxstar:1378175878327959675> **Gift para reais:** \n" 
                    "> Calcula o valor do gift desejado em reais."
                    ),
                    color = 0x54AB4B
                )
            
            view = View(timeout = None)

            botao3 = Button(label = "Gift para Reais", style = ButtonStyle.green)

            async def callback3(interaction: Interaction):
                await interaction.response.send_modal(GiftParaReais(self.bot))

            botao3.callback = callback3

            view.add_item(botao3)


        await interaction.response.send_message(embed = embed, view = view, ephemeral = True)

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
