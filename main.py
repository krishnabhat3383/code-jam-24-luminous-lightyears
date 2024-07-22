from os import getenv
from sys import exit

from dotenv import load_dotenv
from interactions import (
    Client,
    Intents,
    listen,
)

bot = Client(intents=Intents.DEFAULT)


@listen()
async def on_ready() -> None:
    """Print "Ready", when the bot is accepting commands."""
    print("Ready")


load_dotenv()
token = getenv("DEFCON_BOT_TOKEN")

if token is None:
    print("Token not found.\nPlease specify discord bot token via environment variable 'DEFCON_BOT_TOKEN'.")
    exit()

bot.load_extension("src.game_start")
bot.start(token)
