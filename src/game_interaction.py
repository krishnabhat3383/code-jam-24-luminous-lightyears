import random
from string import ascii_uppercase, digits
from typing import TYPE_CHECKING
from interactions import (
    Embed,
    Extension,
    OptionType,
    SlashContext,
    slash_command,
    slash_option,
)

from src.game import Game, GameID

if TYPE_CHECKING:
    from interactions import Client


class GameFactory:
    def __init__(self) -> None:
        self.store: dict[GameID, Game] = {}

    def generate_game_id(self) -> GameID:
        while True:
            game_id = "".join(random.choice(ascii_uppercase + digits) for i in range(12))  # noqa: S311 This isn't for crypto purposes

            if game_id in self.store:
                continue

            return game_id

    def create_game(self) -> Game:
        game_id = self.generate_game_id()
        game = Game(game_id)
        self.store[game_id] = game

        return game

    def query_game(self, game_id: GameID) -> Game | None:
        return self.store.get(game_id, None)

    def query_game_by_playerID(self, player_id) -> Game | None:
        for game in self.store.values():
            if player_id in game.players.keys():
                return game
        

class GameInteraction(Extension):
    """Control the extension entry point."""

    def __init__(self, _: "Client") -> None:
        self.game_factory = GameFactory()

    @slash_command(name="defcord", description="Interact with defcord.")
    async def defcord(ctx:SlashContext) -> None:
        """Make the subcommand work, since it requires a function to latch off of."""
        pass

    @defcord.subcommand(sub_cmd_name="create", sub_cmd_description="Create a game of Defcord")
    async def create(self, ctx: SlashContext) -> None:
        """Create a game of DEFCORD."""
        game = self.game_factory.create_game()  # Add the first player here

        await game.add_player(ctx)

        embed = Embed(
            title="New game started!",
            description=f"Your invite: {game.id}",
            color=(255, 0, 0),
        )

        await ctx.send(embed=embed)


    @defcord.subcommand(sub_cmd_name="Join", sub_cmd_description="Join a game of Defcord")
    @slash_option("invite", "The invite code for the game", required=True, opt_type=OptionType.STRING)
    async def join(self, ctx: SlashContext, invite: str) -> None:
        """Join a game of DEFCORD."""
        game = self.game_factory.query_game(invite)

        if game is None:
            raise NotImplementedError

        await game.add_player(ctx)


    @defcord.subcommand(sub_cmd_name="Leave", sub_cmd_description="Leave a game of Defcord")
    async def leave(self, ctx: SlashContext) -> None:
        """Leave the current game of defcord"""
        game = self.game_factory.query_game_by_playerID(ctx.user.id)
        
        if game is None:
            raise NotImplementedError
        
        await game.remove_player(ctx)
        