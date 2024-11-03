import discord
from discord import app_commands
from discord.ext import commands

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # /avatar 슬래시 명령어 정의
    @app_commands.command(name="avatar", description="유저의 아바타를 고화질로 보여줍니다.")
    async def avatar(self, interaction: discord.Interaction, member: discord.Member = None):
        # 유저가 지정되지 않으면 명령어를 호출한 유저를 기본값으로 설정
        if member is None:
            member = interaction.user

        # 아바타 URL 생성 (최대 해상도 4096)
        avatar_url = member.avatar.url if member.avatar else member.default_avatar.url

        # 임베드 생성
        embed = discord.Embed(
            title=f"{member.display_name}님의 아바타",
            color=discord.Color.random()
        )
        embed.set_image(url=avatar_url)  # 아바타 URL을 임베드에 설정

        await interaction.response.send_message(embed=embed)

# cog를 추가하는 함수
async def setup(bot):
    await bot.add_cog(Avatar(bot))
