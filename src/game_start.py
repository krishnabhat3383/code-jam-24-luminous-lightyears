import random
from asyncio import create_task
from string import ascii_uppercase, digits
from typing import TYPE_CHECKING, Annotated

from interactions import (
    Embed,
    Extension,
    Modal,
    ModalContext,
    OptionType,
    ShortText,
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


class GameInitializon(Extension):
    """Control the extension entry point."""

    def __init__(self, _: "Client") -> None:
        self.game_factory = GameFactory()

    @slash_command(name="defcord_create", description="Create a new DEFCORD game.")
    async def create(self, ctx: SlashContext) -> None:
        """Create a game of DEFCORD."""
        game = self.game_factory.create_game()  # Add the first player here
        nation_name = await self.register_player(ctx)

        await game.add_player(ctx, nation_name)

        embed = Embed(
            title="New game started!",
            description=f"Your invite: {game.id}",
            color=(255, 0, 0),
        )

        await ctx.send(embed=embed)

    @slash_command(name="defcord_join", description="Join a game of DEFCORD.")
    @slash_option("invite", "The invite code for the game", required=True, opt_type=OptionType.STRING)
    async def join(self, ctx: SlashContext, invite: str) -> None:
        """Join a game of DEFCORD."""
        game = self.game_factory.query_game(invite)

        if game is None:
            raise NotImplementedError

        nation_name = await self.register_player()
        await game.add_player(ctx, nation_name)  # Ask nation name here

    async def register_player(self, ctx: SlashContext) -> Annotated[str, "Nation name"]:
        """Ask the player for information."""
        nation_name_modal = Modal(
            ShortText(
                label="Provide your nation name",
                custom_id="nation_name",
                min_length=3,
                max_length=50,
                required=True,
            ),
            title="Player Information",
        )
        await ctx.send_modal(modal=nation_name_modal)

        modal_ctx: ModalContext = await ctx.bot.wait_for_modal(nation_name_modal)
        nation_name = modal_ctx.responses["nation_name"]

        await modal_ctx.send(f"<@{ctx.user.id}> You are playing as a leader of {nation_name}", ephemeral=True)

        return nation_name
