from collections.abc import Callable
from typing import TYPE_CHECKING, Any, Literal, get_args

from attrs import asdict, field, frozen
from interactions import ActionRow, Button, ButtonStyle, Embed

from src.weighted_random import WeightedList

if TYPE_CHECKING:
    from src.player import Player, PlayerState

Consequence = dict[Any, Any]
Condition = Callable[["PlayerState"], bool] | None
Stage = Literal[1, 2, 3]  # Adjustable


@frozen
class Template:
    """Make a template for the messages to be served."""

    text: str = field()
    weight: int = 100
    condition: Condition | None = None

    def format(self, state: "PlayerState") -> str:
        """Format the text."""
        return self.text.format(**asdict(state))

    def is_available(self, state: "PlayerState") -> bool:
        if self.condition is not None:
            return self.condition(state)

        return True

    def to_embed(self, player: "Player", actor: "Actor") -> Embed:
        """Get an embed for UI."""
        # Now you can access actor here
        return Embed(
            title=f"{actor.name} of {player.state.nation_name}",
            description=self.format(player.state),
            color=(0, 0, 255),
        )

    async def ui(self, player: "Player", actor: "Actor") -> None:
        await player.ctx.send(embed=self.to_embed(player, actor), ephemeral=True)


def not_none(var: Any | None) -> Any:  # noqa: ANN401 temporary workaround FIXME
    if var is None:
        raise AttributeError

    return var


@frozen
class ChoiceTemplate(Template):
    choices: dict[str, Consequence] = field(default=None, converter=not_none)  # Specify button color here somehow.

    async def ui(self, player: "Player", actor: "Actor") -> None:
        """Send UI and apply consequences."""
        buttons: list[Button] = []

        for id, choice in enumerate(self.choices.items()):
            button = Button(
                label=f"{next(iter(choice))}",
                style=ButtonStyle.BLURPLE,
                custom_id=f"Choice {id}",
            )
            buttons.append(button)

        embed = self.to_embed(player, actor)

        await player.ctx.send(embed=embed, components=ActionRow(*buttons), ephemeral=True)


total_stages = get_args(Stage)


@frozen
class StageGroup:
    """A helper class to group templates based on their stage in game."""

    @staticmethod
    def convert_stage(stage: Stage | list[Stage] | Literal["all"]) -> list[Stage]:
        if stage == "all":
            return list(total_stages)
        if isinstance(stage, int):
            return [stage]

        return stage

    stage: Stage | list[Stage] | Literal["all"] = field(converter=convert_stage)
    templates: list[Template]


@frozen
class Actor:
    @staticmethod
    def cast_stages(stage_groups: list[StageGroup]) -> dict[Stage, WeightedList[Template]]:
        stages: dict[Stage, WeightedList[Template]] = {}

        for stage_slot in total_stages:
            stage_templates = []

            for stage_group in stage_groups:
                if stage_slot in stage_group.stage:
                    stage_templates += stage_group.templates

            stages[stage_slot] = WeightedList(stage_templates)

        return stages

    name: str
    picture: str
    stages: dict[Stage, WeightedList[Template]] = field(converter=cast_stages)
    weight: int = 100

    def is_available(self, state: "PlayerState") -> bool:
        # Add stuff here if you want to add actors which appear on condition.
        _ = state
        return True

    async def send(self, target: "Player") -> None:
        stage = self.stages[target.game.stage]
        template = stage.get_random(target.state)
        await template.ui(target, self)
