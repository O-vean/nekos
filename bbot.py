import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio

# .env 파일의 환경 변수를 불러옵니다.
load_dotenv()
TOKEN = os.getenv("TOKEN")

# discord.Bot 인스턴스 생성 (슬래시 명령어 지원)
class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents, application_id=os.getenv("DISCORD_APP_ID"))

    async def setup_hook(self):
        # cogs 폴더의 모든 코그 파일을 로드
        cogs_folder = os.path.join(os.path.dirname(__file__), "cogs")
        for filename in os.listdir(cogs_folder):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")
        
        # 슬래시 명령어를 동기화
        await bot.tree.sync()

# 봇 실행 부분
bot = MyBot()

async def main():
    async with bot:
        await bot.start(TOKEN)  # 봇 실행

# 비동기 루프 실행
asyncio.run(main())
