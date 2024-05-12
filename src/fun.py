import nextcord
from nextcord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0xa8b5e0

    @nextcord.slash_command(description="Flip a coin!")
    async def coinflip(self, interaction):
        avatar = str(self.bot.user.avatar.url)

        result = random.choice(['Heads', 'Tails'])
        embed = nextcord.Embed(
            title="Coin Flip Result",
            color=self.color,
            description=f"The coin landed on: {result}"
        )
        embed.set_thumbnail(url=avatar)

        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))
