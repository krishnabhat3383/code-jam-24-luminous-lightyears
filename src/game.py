from interactions import User

from src.models import State

GameID = str


class Game:
    def __init__(self, id: GameID) -> None:
        self.id = id
        self.players: dict[str, State] = {}

    async def add_player(self, user: User, nation_name: str) -> None:
        self.players[user.id] = State(nation_name)
