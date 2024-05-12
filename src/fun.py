import nextcord
from nextcord.ext import commands
import requests
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

    @nextcord.slash_command(description="Send a random discussion topic in chat")
    async def topic(self, interaction):
        topics = ["What's your favorite movie?", "If you could travel anywhere, where would you go?", "What's the last book you read?", "What's your dream job?", "Do you prefer cats or dogs?"]
        random_topic = random.choice(topics)
        await interaction.response.send_message(random_topic)

    @nextcord.slash_command(description="Get NASA's Astronomy Picture of the Day (APOD)")
    async def apod(self, interaction):
        apod_url = "https://api.nasa.gov/planetary/apod"

        params = {
            "api_key": "DaQLr5mVINIQC0j9RdvaXfbksLM9EytyvDoSvNCQ"
        }

        response = requests.get(apod_url, params=params)

        if response.status_code == 200:
            data = response.json()

            title = data["title"]
            explanation = data["explanation"]
            image_url = data["url"]

            embed = nextcord.Embed(
                title=title,
                description=explanation,
                color=self.color
            )
            embed.set_image(url=image_url)

            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("Failed to fetch APOD. Please try again later.")

    @nextcord.slash_command(description="Get a random cat photo")
    async def cat(self, interaction):
        cat_url = "https://api.thecatapi.com/v1/images/search"

        response = requests.get(cat_url)

        if response.status_code == 200:
            data = response.json()
            image_url = data[0]["url"]

            embed = nextcord.Embed(
                title="Random Cat Photo",
                color=self.color
            )
            embed.set_image(url=image_url)

            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("Failed to fetch a cat photo. Please try again later.")

    @nextcord.slash_command(description="Get a random dog photo")
    async def dog(self, interaction):
        dog_url = "https://dog.ceo/api/breeds/image/random"

        response = requests.get(dog_url)

        if response.status_code == 200:
            data = response.json()
            image_url = data["message"]

            embed = nextcord.Embed(
                title="Random Dog Photo",
                color=self.color
            )
            embed.set_image(url=image_url)

            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("Failed to fetch a dog photo. Please try again later.")

def setup(bot):
    bot.add_cog(Fun(bot))
