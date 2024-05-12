import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption
from datetime import datetime

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0xa8b5e0
    
    # Kick command
    @nextcord.slash_command(description="Kicks a member from the server.")
    async def kick(
        self,
        interaction: Interaction,
        member: Member = SlashOption(description="The member to kick."),
        reason: str = SlashOption(description="The reason for kicking.", required=False, default="No reason provided.")
    ):
        if not interaction.user.guild_permissions.kick_members:
            embed = nextcord.Embed(
                title="Error",
                color=self.color,
                description="""
                **No Permission**
                > * **Err:** You don't have permission to kick members
                """)
            await interaction.response.send_message(embed=embed)
            return
        try:
            await member.kick(reason=reason)
            
            embed = nextcord.Embed(
                title="Kick",
                color=self.color,
                description=f"""
                **Kicked**
                > * **User:** {member.mention}
                > * **Reason:** {reason}
                > * **ID:** {member.id}
                > * **Kick successful!**
                """)
            await interaction.response.send_message(embed=embed)
        except nextcord.Forbidden:
            embed = nextcord.Embed(
                title="Error",
                color=self.color,
                description="""
                **No Permission**
                > * **Err:** I don't have permission to kick members
                """)
            await interaction.response.send_message(embed=embed)
            
    # Ban command
    
    # Uban command
    
    # Purge
        
def setup(bot):
    bot.add_cog(Moderation(bot))