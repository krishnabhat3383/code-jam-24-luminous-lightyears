from interactions import User

from models import State

GameID = str

# Tasks to be achieved here 
# 1) Create the game flow, and when the template objects would be called 
# 2) Make an internal game, so we can start testing

class Game:
    def __init__(self, id: GameID) -> None:
        self.id = id
        self.players: dict[str, State] = {}

    async def add_player(self, user: User, nation_name: str) -> None:
        self.players[user.id] = State(nation_name)

    async def remove_player(self, user:User) -> None:
        del self.players[user.id]
