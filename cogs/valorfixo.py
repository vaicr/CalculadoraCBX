import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

class DefinirValorFixo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @nextcord.slash_command(
            name = "valorfixo",
            description = "Defina o valor fixo da unidade de robux ou gift.",
            default_member_permissions = nextcord.Permissions(administrator = True)
    )
    async def valorfixo(self, interaction: Interaction):
        pass

    @valorfixo.subcommand(name = "robux", description = "Estabelece o valor fixo da unidade de robux.")
    async def valorfixo_robux(
        self,
        interaction: Interaction,
        unidade_robux: str = SlashOption(description = "Valor fixo da unidade de robux", required = True)
    ):
        
        await interaction.response.defer(ephemeral = True)

        valor = float(unidade_robux.replace(",", "."))
        self.bot.unidade_robux = valor
        unidade_robux = f"{valor:.3f}".replace(".", ",")
        
        await interaction.followup.send(
            f"Agora, o valor fixo da unidade de robux é **R${unidade_robux}**."
        )

    @valorfixo.subcommand(name = "gift", description = "Estabelece o valor fixo da unidade de gift.")
    async def valorfixo_gift(
        self,
        interaction: Interaction,
        unidade_gift: str = SlashOption(description = "Valor fixo da unidade de gift", required = True)
    ):
        
        await interaction.response.defer(ephemeral = True)

        valor = float(unidade_gift.replace(",", "."))
        self.bot.unidade_gift = valor
        unidade_gift = f"{valor:.3f}".replace(".", ",")

        await interaction.followup.send(
            f"Agora, o valor fixo da unidade de gift é **R${unidade_gift}**."
        )

def setup(bot):
    bot.add_cog(DefinirValorFixo(bot))