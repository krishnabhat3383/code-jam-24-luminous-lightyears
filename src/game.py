import asyncio


from attrs import define
import random
from datetime import datetime, timedelta
from typing import TYPE_CHECKING, Annotated

from interactions import SlashContext
from src.characters import all_characters
from src.const import error_embed
from src.player import Player
from src.templating import total_stages

if TYPE_CHECKING:
    from src.templating import Stage

class Player:
    """Define and register the data related to the player."""

    def __init__(self, ctx: SlashContext, game: "Game") -> None:
        self.ctx = ctx
        self.state: PlayerState = None  # type: ignore TODO: properly type that state isn't none after register
        self.game = game

GameID = str


class Game:
    """Initialize a Game and it's behaviours."""

    def __init__(self, id: GameID) -> None:
        self.id = id
        self.players: dict[Annotated[int, "discord id"], Player] = {}
        self.stage: Stage = 1
        self.max_time: float = random.uniform(12.5, 16)

        self.cumm_percent_time_per_stage: list[float] = [0.25, 0.6, 1]
        # Percentage of the time spent in the game when the next stage of the time begins (max value 1 = 100%)
        self.values_to_check: list[str] = ["loyalty", "money", "security", "world_opinion"]

    async def add_player(self, ctx: SlashContext) -> None:
        player = Player(ctx, self)
        await player.register()
        self.players[ctx.user.id] = player


    async def remove_player(self, ctx: SlashContext) -> None:
        """Remove player from the game."""
        player_to_delete = ctx.user.id
        try:
            del self.players[player_to_delete]
        except KeyError:
            raise NotImplementedError
        # Need to pass this error to the user, that you are in no game

    async def loop(self) -> None:
        """Define the main loop of the game."""
        self.start_time = datetime.now()

        players = self.players.values()

        while True:
            game_time: float = (datetime.now() - self.start_time) / timedelta(minutes=1)
            if (game_time > self.cumm_percent_time_per_stage[self.stage - 1] * self.max_time) and (
                game_time < self.max_time
            ):
                self.stage = total_stages[
                    total_stages.index(self.stage) + 1
                ]  # This isn't the best, but it won't go out of bounds and doesn't break typing

            try:
                await asyncio.gather(*[self.tick(player) for player in players], return_exceptions=True)
            except Exception:  # noqa: BLE001 this is intentional
                for player in players:
                    await player.ctx.send(embed=error_embed)

    async def tick(self, player: Player) -> None:
        """Define the activities done in every game tick."""
        character = all_characters.get_random(player.state)
        # The sleep times are subject to change, based on how the actual gameplay feels
        # The randomness gives a variability between the values mentioned in the brackets
        if any(getattr(player.state, attr) < 0 for attr in self.values_to_check):
            # Some value is negative hence need to send the losing message
            raise NotImplementedError

        match self.stage:
            case 1:
                sleep_time = 10 + (random.uniform(-2, 2))

            case 2:
                sleep_time = 8 + (random.uniform(-2, 1.5))

            case 3:
                sleep_time = 6 + (random.uniform(-1, 0.75))

        await asyncio.sleep(sleep_time)
        await character.send(player)
