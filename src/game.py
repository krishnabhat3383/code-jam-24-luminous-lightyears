from typing import Annotated

from attrs import define
from interactions import SlashContext

from models import State

GameID = str


@define
class Player:
    ctx: SlashContext
    state: State


class Game:
    def __init__(self, id: GameID) -> None:
        self.id = id
        self.players: dict[Annotated[int, "discord id"], Player] = {}

    async def add_player(self, context: SlashContext, nation_name: str) -> None:
        self.players[context.user.id] = Player(context, State(nation_name))

    async def loop(self) -> None: ...
