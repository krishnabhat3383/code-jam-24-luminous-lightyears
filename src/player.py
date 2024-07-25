import typing

from attrs import define
from interactions import Modal, ModalContext, ShortText, SlashContext

if typing.TYPE_CHECKING:
    from src.game import Game


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
