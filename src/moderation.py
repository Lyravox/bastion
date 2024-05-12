from typing import Optional
import nextcord
import re
from nextcord.ext import commands


def parse_user_id(id: str):
    if id.isnumeric():
        return int(id)

    if re.match(r'<@\!?\d+>', id):
        res = re.search(r'\d+', id)
        return int(res.groups()[0]) if res else None

    return None


class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.color = 0xA8B5E0

    @nextcord.slash_command(description="Kick a user",
                            guild_ids=[1239148261223174184])
    async def kick(self,
                   interaction: nextcord.Interaction,
                   user: str,
                   reason: Optional[str] = None):
        embed = nextcord.embeds.Embed()

        if not interaction.guild:
            embed.description = 'This command can only be used in guild'
            return await interaction.response.send_message(embed=embed)

        if not interaction.user.guild_permissions.kick_members:
            embed.description = 'You do not have enough permissions to kick the user'
            return await interaction.response.send_message(embed=embed)

        if not user.isnumeric():
            embed.description = f'User id `{user}` is not valid'
            return await interaction.response.send_message(embed=embed)

        id = parse_user_id(user)

        if not id:
            embed.description = f'Invalid user id `{user}` was given'
            return await interaction.response.send_message(embed=embed)

        target = interaction.guild.get_member(id)

        if not target:
            embed.description = f'No user with ID `{user}` found'
            return await interaction.response.send_message(embed=embed)

        if target.id == interaction.user.id or target.guild_permissions.administrator:
            embed.description = 'The bot doesn\'t have enough permisison to kick the user'
            return await interaction.response.send_message(embed=embed)

        await interaction.guild.kick(target, reason=reason)

        embed = nextcord.embeds.Embed()
        embed.description = f'Kicked user `{target.name}` from server\nReason: `{reason}`'
        embed.color = self.color

        print(f'Kicked `{target.id}` from server')
        return await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(description="Ban a user",
                            guild_ids=[1239148261223174184])
    async def ban(self,
                  interaction: nextcord.Interaction,
                  user: str,
                  reason: Optional[str] = None):
        embed = nextcord.embeds.Embed()

        if not interaction.guild:
            embed.description = 'This command can only be used in guild'
            return await interaction.response.send_message(embed=embed)

        if not interaction.user.guild_permissions.ban_members:
            embed.description = 'You do not have enough permissions to ban the user'
            return await interaction.response.send_message(embed=embed)

        if not user.isnumeric():
            embed.description = f'User id `{user}` is not valid'
            return await interaction.response.send_message(embed=embed)

        if not id:
            embed.description = f'Invalid user id `{user}` was given'
            return await interaction.response.send_message(embed=embed)

        target = interaction.guild.get_member(id)

        if not target:
            embed.description = f'No user with ID `{user}` found'
            return await interaction.response.send_message(embed=embed)

        if target.id == interaction.user.id or target.guild_permissions.administrator:
            embed.description = 'The bot doesn\'t have enough permisison to ban the user'
            return await interaction.response.send_message(embed=embed)

        await interaction.guild.ban(target, reason=reason)

        embed = nextcord.embeds.Embed()
        embed.description = f'Banned user `{target.name}` from server\nReason: `{reason}`'
        embed.color = self.color

        print(f'Banned `{target.id}` from server')
        return await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(description="Unban a user",
                            guild_ids=[1239148261223174184])
    async def unban(self,
                    interaction: nextcord.Interaction,
                    user: str,
                    reason: Optional[str] = None):
        embed = nextcord.embeds.Embed()

        if not interaction.guild:
            embed.description = 'This command can only be used in guild'
            return await interaction.response.send_message(embed=embed)

        if not interaction.user.guild_permissions.ban_members:
            embed.description = 'You do not have enough permissions to unban the user'
            return await interaction.response.send_message(embed=embed)

        if not user.isnumeric():
            embed.description = f'User id `{user}` is not valid'
            return await interaction.response.send_message(embed=embed)

        if not id:
            embed.description = f'Invalid user id `{user}` was given'
            return await interaction.response.send_message(embed=embed)

        target = interaction.client.get_user(id)

        if not target:
            embed.description = f'No user with ID `{user}` found'
            return await interaction.response.send_message(embed=embed)

        await interaction.guild.unban(target, reason=reason)

        embed = nextcord.embeds.Embed()
        embed.description = f'Unbanned user `{target.name}` from server\nReason: `{reason}`'
        embed.color = self.color

        print(f'Unbanned `{target.id}` from server')
        return await interaction.response.send_message(embed=embed)


def setup(bot):
    print('Loading command group: Moderation')
    bot.add_cog(Moderation(bot))


def teardown(bot):
    print('Unloading command group: Moderation')
