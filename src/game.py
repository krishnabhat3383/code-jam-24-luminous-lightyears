"""Module responsible for game actions."""

import asyncio
import logging
import random
import time
from typing import TYPE_CHECKING, Annotated

from attrs import asdict
from interactions import Embed, SlashContext

from src.characters import all_characters
from src.const import AFK_TIME, error_color, system_message_color
from src.player import Player
from src.templating import total_stages

if TYPE_CHECKING:
    from src.game_interaction import GameFactory
    from src.templating import Stage


GameID = str
logger = logging.getLogger(__name__)


class Game:
    """Initialize a Game and it's behaviours."""

    def __init__(self, id: GameID, required_no_of_players: int, game_factory: "GameFactory") -> None:
        self.id = id
        self.required_no_of_players: int = required_no_of_players
        self.players: dict[Annotated[int, "discord id"], Player] = {}
        self.stage: Stage = 1
        self.max_time: float = random.uniform(12.5, 16)
        self.started: bool = False
        self.creator_id: int | None = None
        self.game_stop_flag: bool = False
        self.player_component_choice_mapping: dict[str, dict] = {}
        self.game_factory: GameFactory = game_factory
        self.values_to_check: list[str] = ["loyalty", "money", "security", "world_opinion"]

        # Percentage of the time spent in the game when the next stage of the time begins (max value 1 = 100%)
        self.cumm_percent_time_per_stage: list[float] = [0.25, 0.6, 1]

    async def add_player(self, ctx: SlashContext, cmd: str = "create") -> None:
        """Add a player to the game."""
        logger.info(f"Adding player {ctx.user.id} to the game {self.id}")
        if cmd == "create":
            self.creator_id = ctx.user.id
        player = Player(ctx, self)
        await player.register()
        self.players[ctx.user.id] = player

    async def remove_player(self, ctx: SlashContext) -> None:
        """Remove player from the game."""
        player_to_delete = ctx.user.id

        if player_to_delete in self.players:
            del self.players[player_to_delete]

        self.game_factory.remove_player(player_to_delete)

    async def death_player(self, dead_player: Player) -> None:
        """Mark the player as dead."""
        embed = Embed(
            title="We have lost a national leader in the turmoil",
            description=f"{dead_player.state.nation_name} has lost their leadership which was done by <@{dead_player.ctx.user.id}>",  # noqa: E501
            color=system_message_color,
        )

        for key, value in asdict(dead_player.state).items():
            embed.add_field(name=key.capitalize(), value=value)

        for player in self.players.values():
            await player.ctx.send(embed=embed, ephemeral=True)

        await self.remove_player(dead_player.ctx)

        if len(self.players) == 0 and self.started:
            self.stop()
            self.game_factory.remove_game(self.id)

    async def disqualify_player(self, player: Player) -> None:
        """Disqualify inactive player."""
        embed = Embed(
            title="We have lost a national leader due to inactivity.",
            description=f"{player.state.nation_name} has lost their leadership which was done by \n <@{player.ctx.user.id}>",  # noqa: E501
            color=system_message_color,
        )
        for _player in self.players.values():
            await _player.ctx.send(embed=embed, ephemeral=True)

        await self.remove_player(player.ctx)

        if len(self.players) == 0 and self.started:
            self.stop()
            self.game_factory.remove_game(self.id)

    async def stop_game_by_time(self) -> None:
        """End game because the time is up."""
        embed = Embed(
            title="Time Up! Game Over!",
            description=f"Game is over! Because time is up! We have {len(self.players)} survivors! You are one of them!",  # noqa: E501
            color=system_message_color,
        )

        for player in list(self.players.values()):
            await player.ctx.send(embed=embed, ephemeral=True)
            await self.remove_player(player.ctx)

        self.game_factory.remove_game(self.id)

    async def send_stats(self) -> None:
        """Send player stats."""
        for player in self.players.values():
            embed = Embed(
                title="Stats",
                description=f"<@{player.ctx.user.id}> current stats as follows,",
                color=system_message_color,
            )
            for key, value in asdict(player.state).items():
                embed.add_field(name=key.capitalize(), value=value)

            await player.ctx.send(embed=embed, ephemeral=True)

    def stop(self) -> None:
        """Set the stop flag."""
        self.game_stop_flag = True

    async def loop(self) -> None:
        """Define the main loop of the game."""
        self.start_time = time.time()
        players = self.players.values()
        await self.send_stats()

        while True:
            logger.info(f"{len(self.players)} left in game {self.id}")

            if self.game_stop_flag:
                break

            game_time: float = (time.time() - self.start_time) / 60
            if (game_time > self.cumm_percent_time_per_stage[self.stage - 1] * self.max_time) and (
                game_time < self.max_time
            ):
                self.stage = total_stages[total_stages.index(self.stage) + 1]
                await self.send_stats()

            if game_time >= self.max_time:
                logger.info(f"Time is Up! Game {self.id} is over!")
                self.stop()
                await self.stop_game_by_time()
                break

            logger.info(f"{game_time=} {self.stage=} {self.max_time=}")

            try:
                response = await asyncio.gather(*[self.tick(player) for player in players], return_exceptions=True)

                for res in response:
                    if isinstance(res, Exception):
                        logger.error(res)
            except Exception as e:
                logger.exception("Error occurred in game loop")

                for player in players:
                    await player.ctx.send(
                        embed=Embed(
                            title="Some error occured",
                            description=f"{e} \n has occured, please contact the devs if you see this",
                            color=error_color,
                        ),
                    )

    async def tick(self, player: Player) -> None:
        """Define the activities done in every game tick."""
        if self.game_stop_flag:
            return

        if (time.time() - player.last_activity_time) > AFK_TIME:
            await self.disqualify_player(player)
            return

        character = all_characters.get_random(player.state)
        for attr in self.values_to_check:
            if getattr(player.state, attr) <= 0:
                # Some value is negative hence need to send the losing message
                await self.death_player(player)
                return

        # The sleep times are subject to change, based on how the actual gameplay feels
        # The randomness gives a variability between the values mentioned in the brackets
        match self.stage:
            case 1:
                sleep_time = 10 + (random.uniform(-2, 2))
            case 2:
                sleep_time = 8 + (random.uniform(-2, 1.5))
            case 3:
                sleep_time = 6 + (random.uniform(-1, 0.75))

        character = all_characters.get_random(player.state)
        while self.stage not in character.stages:
            character = all_characters.get_random(player.state)

        result = await character.send(player)

        if result:
            await asyncio.sleep(sleep_time)
        else:
            await asyncio.sleep(0.2)
