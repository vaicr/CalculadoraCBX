from nextcord.ext import commands
from nextcord import Interaction
from nextcord.ui import Modal, TextInput
import math

class GiftParaReais(Modal):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(title = "Gift para reais")

        self.gift = TextInput(
            label = "Insira o valor do gift em robux.",
            placeholder = "Exemplo: 1000",
            required = True
        )
        self.add_item(self.gift)
    
    async def callback(self, interaction: Interaction):
        try:
            gift = int(self.gift.value)

            unidadefinal = getattr(self.bot, "unidadefinal_gift", None)
            
            if unidadefinal is None:
                await interaction.response.send_message(
                    "<:a_warning:1371906000239722580> O valor da unidade de gift não foi definido ainda.",
                    ephemeral=True
                )
                return          
            
            if isinstance(unidadefinal, str):
                unidadefinal = unidadefinal.replace(",", ".")
                unidadefinal = float(unidadefinal)

            reais = f"{gift * unidadefinal:.2f}".replace(".", ",")

            await interaction.response.send_message(
                f"- O valor de um **gift de {int(gift)} robux** é **R${reais}**. \n", 
                ephemeral = True
            )

        except ValueError:

            await interaction.response.send_message(
                "<:a_warning:1371906000239722580> Por favor, digite um número válido.",
                ephemeral = True
            )
