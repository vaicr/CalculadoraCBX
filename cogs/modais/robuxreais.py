from nextcord.ext import commands
from nextcord import Interaction
from nextcord.ui import Modal, TextInput
import math

class RobuxParaReais(Modal):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(title = "Robux para reais")

        self.robux = TextInput(
            label = "Insira a quantidade de robux.",
            placeholder = "Exemplo: 1000",
            required = True
        )
        self.add_item(self.robux)
    
    async def callback(self, interaction: Interaction):
        try:
            robux = int(self.robux.value)

            if robux < 200:
                await interaction.response.send_message(
                    "<:a_warning:1371906000239722580> O valor mínimo é **200 Robux**. Tente novamente.",
                    ephemeral = True
                )
                return
            
            unidadefinal = getattr(self.bot, "unidadefinal_robux", None)
            
            if unidadefinal is None:
                await interaction.response.send_message(
                    "<:a_warning:1371906000239722580> O valor da unidade de robux não foi definido ainda.",
                    ephemeral=True
                )
                return          
            
            if isinstance(unidadefinal, str):
                unidadefinal = unidadefinal.replace(",", ".")
                unidadefinal = float(unidadefinal)

            reais = f"{robux * unidadefinal:.2f}".replace(".", ",")

            if robux >= 200 and robux <= 2000:

                taxa = robux * 10 / 7

                await interaction.response.send_message(
                    f"- O valor de **{int(robux)} robux** é **R${reais}**. \n"
                    f"> Valor a ser colocado na gamepass: **{math.ceil(taxa)} robux** \n"
                    "> Lembre-se de __desativar__ os preços regionais!", 
                    ephemeral = True
                )

            elif robux >= 2001 and robux <= 2199:

                taxa1 = (robux - 1000) * 10 / 7
                taxa2 = 1000 * 10 / 7

                await interaction.response.send_message(
                    f"- O valor de **{int(robux)} robux** é **R${reais}**. \n"
                    f"> Valor a ser colocado na 1ª gamepass: **{math.ceil(taxa1)} robux** \n"
                    f"> Valor a ser colocado na 2ª gamepass: **{math.ceil(taxa2)} robux** \n"
                    "> Lembre-se de __desativar__ os preços regionais!", 
                    ephemeral = True
                )

            elif robux >= 2200 and robux <= 4000:

                taxa1 = 2000 * 10 / 7
                taxa2 = (robux - 2000) * 10 / 7

                await interaction.response.send_message(
                    f"- O valor de **{int(robux)} robux** é **R${reais}**. \n"
                    f"> Valor a ser colocado na 1ª gamepass: **{math.ceil(taxa1)} robux** \n"
                    f"> Valor a ser colocado na 2ª gamepass: **{math.ceil(taxa2)} robux** \n"
                    "> Lembre-se de __desativar__ os preços regionais!", 
                    ephemeral = True
                )

            elif robux >= 4001 and robux <= 4199:

                taxa1 = 2000 * 10 / 7
                taxa2 = (robux - 3000) * 10 / 7
                taxa3 = 1000 * 10 / 7

                await interaction.response.send_message(
                    f"- O valor de **{int(robux)} robux** é **R${reais}**. \n"
                    f"> Valor a ser colocado na 1ª gamepass: **{math.ceil(taxa1)} robux** \n"
                    f"> Valor a ser colocado na 2ª gamepass: **{math.ceil(taxa2)} robux** \n"
                    f"> Valor a ser colocado na 3ª gamepass: **{math.ceil(taxa3)} robux** \n"
                    "> Lembre-se de __desativar__ os preços regionais!", 
                    ephemeral = True
                )

            elif robux >= 4200 and robux <= 5000:

                taxa1e2 = 2000 * 10 / 7
                taxa3 = (robux - 4000) * 10 / 7

                await interaction.response.send_message(
                    f"- O valor de **{int(robux)} robux** é **R${reais}**. \n"
                    f"> Valor a ser colocado na 1ª gamepass: **{math.ceil(taxa1e2)} robux** \n"
                    f"> Valor a ser colocado na 2ª gamepass: **{math.ceil(taxa1e2)} robux** \n"
                    f"> Valor a ser colocado na 3ª gamepass: **{math.ceil(taxa3)} robux** \n"
                    "> Lembre-se de __desativar__ os preços regionais!", 
                    ephemeral = True
                )

            elif robux > 5000:

                await interaction.response.send_message(
                    f"- O valor de **{int(robux)} robux** é **R${reais}**. \n"
                    "> O valor máximo por carrinho é 5000 robux. Para prosseguir com sua compra, consulte o suporte em https://discord.com/channels/1187947032183308389/1335372991646924823.",
                    ephemeral = True
                )

        except ValueError:

            await interaction.response.send_message(
                "<:a_warning:1371906000239722580> Por favor, digite um número válido.",
                ephemeral = True
            )
