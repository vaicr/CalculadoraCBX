from nextcord.ext import commands
from nextcord import Interaction
from nextcord.ui import Modal, TextInput
import math

class ReaisParaRobux(Modal):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(title = "Reais para robux")

        self.reais = TextInput(
            label = "Insira a quantia em reais.",
            placeholder = "Exemplo: 50,00",
            required = True
        )
        self.add_item(self.reais)
    
    async def callback(self, interaction: Interaction):
        try:
            reais = float(self.reais.value.replace(",", "."))
            
            unidadefinal = getattr(self.bot, "unidadefinal_robux", None)

            if isinstance(unidadefinal, str):
                unidadefinal = unidadefinal.replace(",", ".")
                unidadefinal = float(unidadefinal)

            if reais < unidadefinal * 200:
                await interaction.response.send_message(
                    "<:a_warning:1371906000239722580> A quantia em reais deve possibilitar a compra de, no mínimo, **200 Robux**. Tente novamente.",
                    ephemeral = True
                )
                return
            
            if unidadefinal is None:
                await interaction.response.send_message(
                    "<:a_warning:1371906000239722580> O valor da unidade de robux não foi definido ainda.",
                    ephemeral=True
                )
                return 

            robux = reais / unidadefinal
            reais = f"{robux * unidadefinal:.2f}".replace(".", ",")

            if robux >= 200 and robux <= 2000:

                taxa = robux * 10 / 7

                await interaction.response.send_message(
                    f"- A quantia de **R${reais}** dará **{int(robux)} robux**. \n"
                    f"> Valor a ser colocado na gamepass: **{math.ceil(taxa)} robux** \n"
                    "> Lembre-se de __desativar__ os preços regionais!", 
                    ephemeral = True
                )

            elif robux >= 2001 and robux <= 2199:

                taxa1 = (robux - 1000) * 10 / 7
                taxa2 = 1000 * 10 / 7

                await interaction.response.send_message(
                    f"- A quantia de **R${reais}** dará **{int(robux)} robux**. \n"
                    f"> Valor a ser colocado na 1ª gamepass: **{math.ceil(taxa1)} robux** \n"
                    f"> Valor a ser colocado na 2ª gamepass: **{math.ceil(taxa2)} robux** \n"
                    "> Lembre-se de __desativar__ os preços regionais!", 
                    ephemeral = True
                )

            elif robux >= 2200 and robux <= 4000:

                taxa1 = 2000 * 10 / 7
                taxa2 = (robux - 2000) * 10 / 7

                await interaction.response.send_message(
                    f"- A quantia de **R${reais}** dará **{int(robux)} robux**. \n"
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
                    f"- A quantia de **R${reais}** dará **{int(robux)} robux**. \n"
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
                    f"- A quantia de **R${reais}** dará **{int(robux)} robux**. \n"
                    f"> Valor a ser colocado na 1ª gamepass: **{math.ceil(taxa1e2)} robux** \n"
                    f"> Valor a ser colocado na 2ª gamepass: **{math.ceil(taxa1e2)} robux** \n"
                    f"> Valor a ser colocado na 3ª gamepass: **{math.ceil(taxa3)} robux** \n"
                    "> Lembre-se de __desativar__ os preços regionais!", 
                    ephemeral = True
                )

            elif robux > 5000:

                await interaction.response.send_message(
                    f"- A quantia de **R${reais}** dará **{int(robux)} robux**. \n"
                    "> O valor máximo por carrinho é 5000 robux. Para prosseguir com sua compra, consulte o suporte em https://discord.com/channels/1187947032183308389/1385692023268315166.",
                    ephemeral = True
                )

        except ValueError:

            await interaction.response.send_message(
                "<:a_warning:1371906000239722580> Por favor, digite um número válido.",
                ephemeral = True
            )
