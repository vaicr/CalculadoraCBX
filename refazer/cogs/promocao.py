import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

class DefinirPromocao(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.promocao = self
        super().__init__()

    @nextcord.slash_command(
        name = "promocao",
        description = "Faça ou retire uma promoção na loja.",
        default_member_permissions = nextcord.Permissions(administrator = True)
    )
    async def promocao(self, interaction: Interaction,):
        pass
         
    @promocao.subcommand(name = "robux", description = "Faça ou retire uma promoção de robux na loja.")

    async def promocao_robux(
        self,
        interaction: Interaction,
        porcentagem: str = SlashOption(description = "Porcentagem de desconto (Ex: 20 para 20%)", required = True)
    ):
        
        unidade_robux = getattr(self.bot, "unidade_robux", None)

        try:
            porcentagem = float(porcentagem.replace(",", "."))
        except ValueError:
            await interaction.response.send_message("<:a_warning:1371906000239722580> Porcentagem inválida.")
            return

        percentual = f"{porcentagem}".replace(".", ",")

        if porcentagem < 0 or porcentagem > 100:
            await interaction.response.send_message("<:a_warning:1371906000239722580> A porcentagem deve estar entre 0 e 100.")
            return
        
        elif unidade_robux is None:
            await interaction.response.send_message("<:a_warning:1371906000239722580> O valor da unidade de robux ainda não foi definido. Use o comando **/valorfixo robux** primeiro.")
            return
        
        unidade_robux = float(unidade_robux)
        
        valorpromocional = unidade_robux * (1 - porcentagem / 100)
        unidadefinal_robux = f"{valorpromocional:.4f}".replace(".", ",")
        milrobux = f"{valorpromocional * 1000:.2f}".replace(".", ",")

        self.bot.unidadefinal_robux = valorpromocional

        if porcentagem == 0:
            await interaction.response.send_message(
                f"- Nenhuma promoção aplicada! \n"
                f"> Valor da unidade de robux: **R${unidadefinal_robux}** \n"
                f"> **1000 robux = R${milrobux}**"
            )
        
        else:
            await interaction.response.send_message(
                f"- Promoção de **{percentual}%** aplicada! \n"
                f"> Agora, o valor da unidade de robux é **R${unidadefinal_robux}**. \n"
                f"> **1000 robux = R${milrobux}**"
            )

    @promocao.subcommand(name = "gift", description = "Faça ou retire uma promoção de gift na loja.")

    async def promocao_gift(
        self,
        interaction: Interaction,
        porcentagem: str = SlashOption(description = "Porcentagem de desconto (Ex: 20 para 20%)", required = True)
    ):
        
        unidade_gift = getattr(self.bot, "unidade_gift", None)

        try:
            porcentagem = float(porcentagem.replace(",", "."))
        except ValueError:
            await interaction.response.send_message("<:a_warning:1371906000239722580> Porcentagem inválida.")
            return

        percentual = f"{porcentagem}".replace(".", ",")

        if porcentagem < 0 or porcentagem > 100:
            await interaction.response.send_message("<:a_warning:1371906000239722580> A porcentagem deve estar entre 0 e 100.")
            return
        
        elif unidade_gift is None:
            await interaction.response.send_message("<:a_warning:1371906000239722580> O valor da unidade de gift ainda não foi definido. Use o comando **/valorfixo gift** primeiro.")
            return
        
        unidade_gift = float(unidade_gift)

        valorpromocional = unidade_gift * (1 - porcentagem / 100)
        unidadefinal_gift = f"{valorpromocional:.4f}".replace(".", ",")
        milrobux = f"{valorpromocional * 1000:.2f}".replace(".", ",")

        self.bot.unidadefinal_gift = valorpromocional

        if porcentagem == 0:
            await interaction.response.send_message(
                f"- Nenhuma promoção aplicada! \n"
                f"> Valor da unidade de gift: **R${unidadefinal_gift}** \n"
                f"> **Gift de 1000 robux = R${milrobux}**"
            )
        
        else:
            await interaction.response.send_message(
                f"- Promoção de **{percentual}%** aplicada! \n"
                f"> Agora, o valor da unidade de gift é **R${unidadefinal_gift}**. \n"
                f"> **Gift de 1000 robux = R${milrobux}**"
            )
            
def setup(bot):
    bot.add_cog(DefinirPromocao(bot))