import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption
from datetime import datetime
import random

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0xa8b5e0
        
    # About command
    @nextcord.slash_command(description="About Bastion!")
    async def about(self, interaction: Interaction):
        avatar = str(self.bot.user.avatar.url)
        members = sum(guild.member_count for guild in self.bot.guilds)
        bot_user = await self.bot.fetch_user(self.bot.user.id)
        banner = bot_user.banner.url
        latency = int(self.bot.latency * 1000)
        
        embed = nextcord.Embed(
            title="About",
            color=self.color,
            description=f"""**Information**
            > * **Name:** Bastion
            > * **Owner:** <@1136085806147182713>
            > * **ID:** {self.bot.user.id}
            > * **Github/Documentation:** https://github.com/Lyravox/bastion
            
            **Statistics**
            > * **Latency:** {latency}ms
            > * **Server Count:** {len(self.bot.guilds)}
            > * **Member Count:** {members}
            """
            )
        embed.set_thumbnail(url=avatar)
        embed.set_image(url=banner)
        
        await interaction.response.send_message(embed=embed)
        
def setup(bot):
    bot.add_cog(Utilities(bot))