import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption
import random
import json
import aiohttp
import asyncio

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0xa8b5e0

    @nextcord.slash_command(description="Flip a coin!")
    async def coinflip(self, interaction: Interaction):
        avatar = str(self.bot.user.avatar.url)

        result = random.choice(['Heads', 'Tails'])
        embed = nextcord.Embed(
            title="Coin Flip",
            color=self.color,
            description=f"""
            **Results**
            > * **Side:** {result}
            """)
        embed.set_thumbnail(url=avatar)

        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(description="Replies with a random topic.")
    async def topic(self, interaction: Interaction):
        with open("src/data/topics.json") as f:
            topics = json.load(f)
            topic = random.choice(topics)
            avatar = str(self.bot.user.avatar.url)

            
            embed = nextcord.Embed(
                title="Topic",
                color=self.color,
                description=f"""
                **Conversation Topic**
                > * **Picked:** {topic} 
                """)
            embed.set_thumbnail(url=avatar)
            
            await interaction.response.send_message(embed=embed)
            
    @nextcord.slash_command(description="Replies with a random cat image.")
    async def cat(self, interaction: Interaction):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.thecatapi.com/v1/images/search") as response:
                if response.status != 200:
                    embed = nextcord.Embed(
                        title="Error",
                        color=self.color,
                        description="""
                        **No Cat Image**
                        > * **Fetch:** Could not fetch a cat image
                        """)
                    return
                data = await response.json()
                if not data or not data[0] or not data[0].get("url"):
                    embed = nextcord.Embed(
                        title="Error",
                        color=self.color,
                        description="""
                        **No Cat Image**
                        > * **Fetch:** Failed to fetch a cat image
                        """)
                    await interaction.response.send_message(embed=embed)
                    return
                url = data[0]["url"]
                
                embed = nextcord.Embed(
                    title="Cat",
                    color=self.color,
                )
                embed.set_image(url=url)
                await interaction.response.send_message(embed=embed)
                
    @nextcord.slash_command(description="Replies with a random dog image.")
    async def dog(self, interaction: Interaction):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.thedogapi.com/v1/images/search") as response:
                if response.status != 200:
                    embed = nextcord.Embed(
                        title="Error",
                        color=self.color,
                        description="""
                        **No Dog Image**
                        > * **Fetch:** Could not fetch a dog image
                        """)
                    return
                data = await response.json()
                if not data or not data[0] or not data[0].get("url"):
                    embed = nextcord.Embed(
                        title="Error",
                        color=self.color,
                        description="""
                        **No Dog Image**
                        > * **Fetch:** Failed to fetch a dog image
                        """)
                    await interaction.response.send_message(embed=embed)
                    return
                url = data[0]["url"]
                
                embed = nextcord.Embed(
                    title="Dog",
                    color=self.color,
                )
                embed.set_image(url=url)
                await interaction.response.send_message(embed=embed)
        
def setup(bot):
    bot.add_cog(Fun(bot))