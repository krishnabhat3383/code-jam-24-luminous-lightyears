
from collections.abc import Callable
from typing import Any, Literal, get_args

from attrs import asdict, define, field, frozen
from interactions import ActionRow, Button, ButtonStyle, Embed

Stage = Literal[1, 2, 3]  # Adjustable


@define
class State:
    """State the current state of the player."""

    nation_name: str
    stage: Stage = 1

    money: int = 100
    loyalty: int = 50
    some_other_thing: int = 0

    def apply(self, consequence: dict) -> None:
        """Apply the condition."""
        for k, v in consequence.items():
            self.__dict__[k] += v


Consequence = dict[Any, Any]
Condition = Callable[[State], bool] | None


@frozen
class Template:
    """Make a template for the messages to be served."""

    @staticmethod
    def convert_condition(condition: Condition | None) -> Condition:
        """Convert based on the condition."""
        def always_true(_: State) -> True:
            """Return True."""
            return True

        if condition is None:
            return always_true

        return condition

    text: str
    choices: dict[None, Consequence]
    condition: Condition = field(converter=convert_condition)

    def format(self, state: State) -> str:
        """Format the text."""
        return self.text.format(asdict(state))

    def to_embed(self, state: State) -> list[Embed, ActionRow]:
        """Return embed and action row for the UI purpose."""
        buttons: list[Button] = []
        for id, choice in enumerate(self.choices):
            button = Button(
                label=f"{next(iter(choice.keys()))}",
                ButtonStyle=ButtonStyle.BLURPLE,
                custom_id=f"Choice {id}",
            )
            buttons.append(button)
        action_row = ActionRow(*buttons)
        embed = Embed(
            title=state.nation_name,
            description=self.text,
            color=(0, 0, 255),
            # Can we access Actor here in this class? like this actor is saying this
        )
        return [embed, action_row]

TotalStages = get_args(Stage)


@frozen
class StageGroup:
    """State Stage Group."""

    stage: Stage | tuple[Stage] | Literal["all"] = field(
        converter=lambda stage: TotalStages if stage == "all" else stage,
    )
    templates: list[Template]


@frozen
class Actor:
    """State Actor."""

    name: str
    picture: str  # we'll need to serve these as static content probably
    templates: list[StageGroup]
