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
    """Game creator factory class."""

    def __init__(self) -> None:
        self.games: dict[GameID, Game] = {}
        self.players: dict[int, Game] = {}

    def generate_game_id(self) -> GameID:
        """Generate a random id for the game."""
        while True:
            game_id = "".join(random.choice(ascii_uppercase + digits) for i in range(6))

            if game_id in self.games:
                continue

            return game_id

    def create_game(self, required_no_of_players: int) -> Game:
        """Create a game with the required details."""
        game_id = self.generate_game_id()
        game = Game(game_id, required_no_of_players)
        self.games[game_id] = game

        return game

    def add_player(self, player_id: int, game: Game) -> None:
        """Map a player with a game."""
        self.players[player_id] = game

    def remove_player(self, player_id: int) -> None:
        """Remove a player game mapping."""
        del self.players[player_id]

    def remove_game(self, game_id: int) -> None:
        """Remove a game from game id mapping."""
        del self.games[game_id]

    def query_game(self, game_id: GameID | None = None, player_id: int | None = None) -> Game | None:
        """Return the game based on the query details."""
        if game_id:
            return self.games.get(game_id, None)
        if player_id:
            return self.players.get(player_id, None)

        err = "You need to specify either game_id or player_id"
        raise AttributeError(err)


class GameInteraction(Extension):
    """Control the extension entry point."""

    def __init__(self, _: "Client") -> None:
        self.game_factory = GameFactory()

    async def send_player_join_notification(self, game: Game, ctx: SlashContext) -> None:
        """Send a notification to all the players that a player has joined the game."""
        for player in game.players.values():
            remaining_players_count = game.required_no_of_players - len(game.players)
            if remaining_players_count:
                count_message = f"{remaining_players_count} yet to join."
            else:
                count_message = "All aboard. The game creator can start the game now."

            await player.ctx.send(
                f"<@{ctx.user.id}> joined the game.\n{count_message}",
                ephemeral=True,
            )

    @slash_command(name="defcord", description="Interact with defcord.")
    async def defcord(self, ctx: SlashContext) -> None:
        """Make the subcommand work, since it requires a function to latch off of."""

    @defcord.subcommand(sub_cmd_name="create", sub_cmd_description="Create a game of Defcord")
    @slash_option(
        "required_no_of_players",
        "Number of players required for the game",
        required=True,
        opt_type=OptionType.INTEGER,
        min_value=1,
        max_value=10,
    )
    async def create(self, ctx: SlashContext, required_no_of_players: int = 5) -> None:
        """Create a game of DEFCORD."""
        existing_game = self.game_factory.query_game(player_id=ctx.user.id)
        if existing_game:
            await ctx.send(
                f"<@{ctx.user.id}> You are already part of the game with invite {existing_game.id}",
                ephemeral=True,
            )
            return

        game = self.game_factory.create_game(required_no_of_players)
        self.game_factory.add_player(ctx.user.id, game)
        await game.add_player(ctx, cmd="create")

        embed = Embed(
            title="New game started!",
            description=f"Your invite: {game.id}",
            color=(255, 0, 0),
        )

        await ctx.send(embed=embed)
        await self.send_player_join_notification(game, ctx)

    @defcord.subcommand(sub_cmd_name="join", sub_cmd_description="Join a game of Defcord")
    @slash_option("invite", "The invite code for the game", required=True, opt_type=OptionType.STRING)
    async def join(self, ctx: SlashContext, invite: str) -> None:
        """Join a game of DEFCORD."""
        game = self.game_factory.query_game(game_id=invite)

        if game is None:
            await ctx.send(f"<@{ctx.user.id}> Invite({invite}) is invalid", ephemeral=True)
            return

        if ctx.user.id in game.players:
            await ctx.send(f"<@{ctx.user.id}> You are already part of the game with {invite=}", ephemeral=True)
            return

        if game.required_no_of_players == len(game.players):
            await ctx.send(f"<@{ctx.user.id}> Game is already full {invite=}", ephemeral=True)
            return

        if game.started:
            await ctx.send(f"<@{ctx.user.id}> Game already started", ephemeral=True)
            return

        self.game_factory.add_player(ctx.user.id, game)
        await game.add_player(ctx, cmd="join")
        await self.send_player_join_notification(game, ctx)

    @defcord.subcommand(sub_cmd_name="leave", sub_cmd_description="Leave a game of Defcord")
    async def leave(self, ctx: SlashContext) -> None:
        """Leave the current game of defcord."""
        game = self.game_factory.query_game(player_id=ctx.user.id)

        if game is None:
            await ctx.send(f"<@{ctx.user.id}> You are not part of any game", ephemeral=True)
            return

        # if game.creator == ctx.user.id: # TODO: check this validity - needed of not
        #     await ctx.send(f"<@{ctx.user.id}> Game creator cannot leave the game", ephemeral=True)  # noqa: ERA001
        #     return  # noqa: ERA001

        self.game_factory.remove_player(ctx.user.id)
        await game.remove_player(ctx)

        embed = Embed(
            title="A Player left the game",
            description=f"<@{ctx.user.id}> has left the game ({len(game.players)} players left).",
            color=(255, 0, 0),
        )
        for player in game.players.values():
            await player.ctx.send(embed=embed, ephemeral=True)

        await ctx.send(embed=embed, ephemeral=True)

        if len(game.players) == 0:
            await ctx.send("Game Over! You are the only one survivor. Everyone quit!", ephemeral=True)
            game.stop()
            self.game_factory.remove_game(game.id)

    @defcord.subcommand(sub_cmd_name="start", sub_cmd_description="Start a game of DEFCORD.")
    async def start(self, ctx: SlashContext) -> None:
        """Start and runs the Defcord game loop."""
        game = self.game_factory.query_game(player_id=ctx.user.id)

        if game is None:
            await ctx.send(f"<@{ctx.user.id}> You are not part of any game", ephemeral=True)
            return

        if game.creator != ctx.user.id:
            await ctx.send(f"<@{ctx.user.id}> Only game creator can start it", ephemeral=True)
            return

        if game.started:
            await ctx.send(f"<@{ctx.user.id}> Game already started", ephemeral=True)
            return

        if game.required_no_of_players != len(game.players):
            await ctx.send(f"<@{ctx.user.id}> Cannot start the game until all the players join", ephemeral=True)
            return

        game.started = True
        await ctx.send(f"<@{ctx.user.id}> Game started", ephemeral=True)
        await game.loop()
