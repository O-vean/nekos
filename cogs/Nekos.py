import discord
from discord import app_commands
from discord.ext import commands
import requests

class NekosBest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # /neko 슬래시 명령어 정의
    @app_commands.command(name="neko", description="랜덤 Neko 이미지를 보여줍니다.")
    async def neko(self, interaction: discord.Interaction):
        # API 엔드포인트에서 랜덤 Neko 이미지 가져오기
        url = "https://nekos.best/api/v2/neko"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            image_url = data["results"][0]["url"]
            anime_name = data["results"][0].get("anime_name", "Unknown Anime")
            artist_name = data["results"][0].get("artist_name", "Unknown Artist")

            # 임베드 생성
            embed = discord.Embed(
                title="랜덤 Neko 이미지",
                description=f"Anime: {anime_name}\nArtist: {artist_name}",
                color=discord.Color.purple()
            )
            embed.set_image(url=image_url)

            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("이미지를 가져오는 데 실패했습니다. 나중에 다시 시도해 주세요.", ephemeral=True)

# cog를 추가하는 함수
async def setup(bot):
    await bot.add_cog(NekosBest(bot))
