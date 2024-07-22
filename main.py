import logging
from os import getenv
from sys import exit

from dotenv import load_dotenv
from interactions import (
    Client,
    Intents,
    listen,
)

log = logging.getLogger("defcon-internal")
bot = Client(intents=Intents.DEFAULT, logging_level=logging.WARNING)


@listen()
async def on_ready() -> None:
    log.info("Bot started.")


load_dotenv()
token = getenv("DEFCON_BOT_TOKEN")

if token is None:
    log.error("Token not found.\nPlease specify discord bot token via environment variable 'DEFCON_BOT_TOKEN'.")
    exit()

bot.load_extension("src.game_start")
bot.start(token)
