from interactions import (
    ActionRow,
    Button,
    ButtonStyle,
    ComponentContext,
    Embed,
    Extension,
    SlashContext,
    component_callback,
    slash_command,
    slash_option,
)

from game import Game, GameID

# Game = dict[Member, State]


class GameManager:
    def __init__(self) -> None:
        self.store: dict[GameID, Game] = {}

    def generate_game_id() -> GameID:
        return "alpha-bravo"  # Generate randomly

    def create_game(self) -> Game:
        game_id = self.generate_game_id()
        game = Game(game_id)
        self.store[game_id] = game

        return Game

    def query_game(self, game_id: GameID) -> Game:
        return self.store.get(game_id, None)


class GameInitializon(Extension):
    """Control the extension entry point."""

    def __init__(self, _) -> None:
        self.manager = GameManager()

    @slash_command(name="defcord_create_game", description="Welcome to the simulation called DEFCORD")
    async def create(self, ctx: SlashContext) -> None:
        game = self.manager.create_game()  # Add the first player here

        embed = Embed(
            title="New game started!",
            description=f"Your invite: {game.id}",
            color=(255, 0, 0),
        )

        await ctx.send(embed=embed)

    @slash_command(name="start_defcord", description="Welcome to the simulation called DEFCORD")
    @slash_option("invite", "The invite code for the game", required=True)
    async def join(self, ctx: SlashContext, invite: str) -> None:
        """Start the game of DEFCORD."""

        game = self.manager.query_game(invite)

        if game is None:
            raise NotImplementedError

        await game.add_player(ctx.user, "")  # Ask nation name here
