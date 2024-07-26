import asyncio
import random
from datetime import datetime, timedelta
from typing import Annotated, Literal

from attrs import define
from interactions import Modal, ModalContext, ShortText, SlashContext

from src.characters import all_characters
from src.utils import error_embed

GameID = str


@define
class PlayerState:
    """The current state of the player."""

    nation_name: str

    # Money with the government
    money: float = 100

    # How loyal people feel to the current government that you have created
    loyalty: float = 50

    # How vulnerable is the country from external threats
    security: float = 50

    # Lower means entity sabotage and vice versa (might add this as a later future)
    world_opinion: float = 50

    def apply(self, consequence: dict) -> None:
        """Apply the consequnces to current state."""
        for k, v in consequence.items():
            self.__dict__[k] += v


class Player:
    """Initialize a Player and it's behaviours."""

    def __init__(self, ctx: SlashContext, game: "Game") -> None:
        self.ctx = ctx
        self.state: PlayerState = None  # type: ignore TODO: properly type that state isn't none after register
        self.game = game

    async def register(self) -> None:
        """Ask the player for information."""
        registration_modal = Modal(
            ShortText(
                label="Provide your nation name",
                custom_id="nation_name",
                min_length=3,
                max_length=50,
                required=True,
            ),
            title="Player Information",
        )
        await self.ctx.send_modal(modal=registration_modal)

        modal_ctx: ModalContext = await self.ctx.bot.wait_for_modal(registration_modal)

        # await modal_ctx.send(f"<@{ctx.user.id}> You are playing as a leader of {nation_name}", ephemeral=True)

        nation_name = modal_ctx.responses["nation_name"]

        self.state = PlayerState(nation_name)


class Game:
    """Initialize a Game and it's behaviours."""

    def __init__(self, id: GameID) -> None:
        self.id = id
        self.players: dict[Annotated[int, "discord id"], Player] = {}
        self.stage: Stage = 1
        self.max_time: float = random.uniform(12.5, 16)

        self.cumm_percent_time_per_stage : list[float]= [0.25, 0.6, 1]
        # Percentage of the time spent in the game when the next stage of the time begins (max value 1 = 100%)


    async def add_player(self, ctx: SlashContext) -> None:
        """Add player to the game."""
        self.players[ctx.user.id] = Player(ctx, self)

    async def loop(self) -> None:
        """Define the main loop of the game."""
        self.start_time = datetime.now()
        players = self.players.values()

        while True:
            game_time :float = (datetime.now() - self.start_time) / timedelta(minutes=1)
            if ((game_time > self.cumm_percent_time_per_stage[self.stage - 1] * self.max_time)
                and (game_time < self.max_time)):
                self.stage += 1
            try:
                await asyncio.gather(*[self.tick(player) for player in players], return_exceptions=True)
            except Exception:  # noqa: BLE001
                for player in players:
                    await player.ctx.send(embed=error_embed)

    async def tick(self, player: Player) -> None:
        """Define the activities done in every game tick."""
        character = all_characters.get_random()
        # The sleep times are subject to change, based on how the actual gameplay feels
        # The randomness gives a variability between the values mentioned in the brackets
        match self.stage:
            case 1:
                asyncio.sleep(15+(random.uniform(-2,2)))
                await character.send(player)

            case 2:
                asyncio.sleep(13+(random.uniform(-2,1.5)))
                await character.send(player)

            case 1:
                asyncio.sleep(10+(random.uniform(-2,1)))
                await character.send(player)

Stage = Literal[1, 2, 3]  # Adjustable
