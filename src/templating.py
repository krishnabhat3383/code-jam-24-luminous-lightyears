import random
from collections.abc import Callable
from typing import Any, Literal, get_args

from attrs import asdict, field, frozen
from interactions import ActionRow, Button, ButtonStyle, Embed

from src.player import Player, PlayerState
from src.weighted_random import WeightedList

Consequence = dict[Any, Any]
Condition = Callable[[PlayerState], bool] | None
Stage = Literal[1, 2, 3]  # Adjustable


@frozen
class Template:
    """Make a template for the messages to be served."""

    text: str = field()
    weight: int = 100

    def format(self, state: PlayerState) -> str:
        """Format the text."""
        return self.text.format(**asdict(state))

    def to_embed(self, player: Player, actor: "Actor") -> Embed:
        """Get an embed for UI."""
        # Now you can access actor here
        return Embed(
            title=f"{actor.name} of {player.state.nation_name}",
            description=self.format(player.state),
            color=(0, 0, 255),
        )

    async def ui(self, player: Player, actor: "Actor") -> None:
        await player.ctx.send(embed=self.to_embed(player, actor), ephemeral=True)


def not_none(var: Any | None) -> Any:  # noqa: ANN401 temporary workaround FIXME
    if var is None:
        raise AttributeError

    return var


@frozen
class ChoiceTemplate(Template):
    choices: dict[str, Consequence] = field(default=None, converter=not_none)  # Specify button color here somehow.
    condition: Condition | None = None

    def is_available(self, player: Player) -> bool:
        if self.condition is not None:
            return self.condition(player.state)

        return True

    async def ui(self, player: Player, actor: "Actor") -> None:
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


class StageData:
    def __init__(self, templates: list[Template]) -> None:
        self.templates = templates
        self.weights = [template.weight for template in self.templates]

    def get_random(self) -> Template:
        return random.choices(self.templates, weights=self.weights, k=1)[0]  # noqa: S311 Not for cryptographic purposes


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

    async def send(self, target: Player) -> None:
        stage = self.stages[target.game.stage]
        template = stage.get_random()
        await template.ui(target, self)
