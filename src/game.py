import asyncio
import typing
from typing import Annotated

from interactions import SlashContext

from src.characters import all_characters
from src.player import Player
from src.utils import error_embed

if typing.TYPE_CHECKING:
    from src.templating import Stage

GameID = str


class Game:
    def __init__(self, id: GameID) -> None:
        self.id = id
        self.players: dict[Annotated[int, "discord id"], Player] = {}
        self.stage: Stage = 1

    async def add_player(self, ctx: SlashContext) -> None:
        self.players[ctx.user.id] = Player(ctx, self)

    async def loop(self) -> None:
        players = self.players.values()

        while True:
            try:
                await asyncio.gather(*[self.tick(player) for player in players], return_exceptions=True)
            except Exception:  # noqa: BLE001
                for player in players:
                    await player.ctx.send(embed=error_embed)

    async def tick(self, player: Player) -> None:
        character = all_characters.get_random()

        await character.send(player)
