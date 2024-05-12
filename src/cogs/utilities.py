import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption
from datetime import datetime
import random

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0xa8b5e0
        
    # Ping command
    @nextcord.slash_command(description="Replies with bot latency.")
    async def ping(self, interaction: Interaction):
        latency = int(self.bot.latency * 1000)
        avatar = self.bot.user.avatar.url
        
        embed = nextcord.Embed(title="Ping", color=self.color, description=f"""**Bot Latency**
                               > * **Latency:** {latency}""")
        embed.set_thumbnail(url=avatar)
        
        await interaction.response.send_message(embed=embed)
        
def setup(bot):
    bot.add_cog(Utilities(bot))