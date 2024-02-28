import main
from nextcord import Interaction
from nextcord.ext import commands

class PingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @main.bot.slash_command(name="ping", description="Responds with 'pong'",guild_ids=())
    async def test(self, Interaction: Interaction):
        await Interaction.response.send_message("pong")

def setup(bot):
    bot.add_cog(PingCog(bot))
