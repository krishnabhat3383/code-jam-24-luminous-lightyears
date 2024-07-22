from os import getenv

from dotenv import load_dotenv
from interactions import (
    Client,
    Intents,
    listen,
)

load_dotenv()
bot = Client(intents=Intents.DEFAULT)


@listen()
async def on_ready() -> None:
    """Print "Ready", when the bot is accepting commands."""
    print("Ready")


bot.load_extension("src.game_start")
bot.start(getenv("BOT_TOKEN"))
