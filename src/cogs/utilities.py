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
        latency = int(self.bot.latency * 1000)
        
        embed = nextcord.Embed(
            title="About",
            color=self.color,
            description=f"""**Information**
            > * **Name:** Bastion
            > * **Owner:** <@1136085806147182713>
            > * **Contributors:** <@1136085806147182713>, <@1020384453694062642>
            > * **ID:** {self.bot.user.id}
            > * **Github/Documentation:** https://github.com/Lyravox/bastion
            
            **Statistics**
            > * **Latency:** {latency}ms
            > * **Server Count:** {len(self.bot.guilds)}
            > * **Member Count:** {members}
            """
            )
        embed.set_thumbnail(url=avatar)
        
        await interaction.response.send_message(embed=embed)
        
    # Server information command
    @nextcord.slash_command(description="Replies with server information.")
    async def server(self, interaction: Interaction):
        server = interaction.guild
        name = server.name
        owner = server.owner.mention
        id = server.id
        creation = int(server.created_at.timestamp())
        timestamp = f"<t:{creation}:F>"
        icon = server.icon.url
        channels = len(server.channels)
        vcs = len(server.voice_channels)
        categories = len(server.categories)
        roles = len(server.roles)
        
        embed = nextcord.Embed(
            title="Server Information",
            color=self.color,
            description=f"""
            **Information**
            > * **Name:** {name}
            > * **Owner:** {owner}
            > * **ID:** {id}
            > * **Creation:** {timestamp}
            
            **Statistics**
            > * **Categories:** {categories}
            > * **Channels:** {channels}
            > * **VCs:** {vcs}
            > * **Roles:** {roles}
            """)
        embed.set_thumbnail(url=icon)
        
        await interaction.response.send_message(embed=embed)
    
    # User command
    @nextcord.slash_command(description="Replies with user information.")
    async def user(self, interaction: Interaction, member: Member = None):
        if member is None:
            member = interaction.user
        avatar = member.avatar.url
        name = member.mention
        id = member.id
        creation = int(member.created_at.timestamp())
        timestamp = f"<t:{creation}:F>"
        
        embed = nextcord.Embed(
            title="User Information",
            color=self.color,
            description=f"""
            **User**
            > * **Name:** {name}
            > * **ID:** {id}
            > * **Creation:** {timestamp}
            """)
        embed.set_thumbnail(url=avatar)
        
        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(description="Rolls some dice")
    async def dice(self, interaction: Interaction, number: int, sides: int):
        avatar = self.bot.user.avatar.url
        if sides < 2:
            embed = nextcord.Embed(
                title="Error",
                color=self.color,
                description="Number of sides must be 2 or more!"
            )
            embed.set_thumbnail(url=avatar)
            await interaction.response.send_message(embed=embed)
            return
        if number > 50:
            embed = nextcord.Embed(
                title="Error",
                color=self.color,
                description="You can only roll up to 50 dice!")
            embed.set_thumbnail(url=avatar)
            await interaction.response.send_message(embed=embed)
            return
        rolls = [random.randint(1, sides) for _ in range(number)]
        result = ', '.join(map(str, rolls))
        total = sum(rolls)
        
        embed = nextcord.Embed(
            title="Dice",
            color=self.color,
            description=f"""
            **Roll**
            > * **Rolled:** {number}d{sides}
            > * **Result:** {result}
            > * **Total:** {total}
            """)
        embed.set_thumbnail(url=avatar)
        
        await interaction.response.send_message(embed=embed)
            
def setup(bot):
    bot.add_cog(Utilities(bot))