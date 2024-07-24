import random
from collections.abc import Callable
from typing import Any, Literal, get_args

from attrs import asdict, field, frozen
from interactions import ActionRow, Button, ButtonStyle, Embed

from game import Player, PlayerState, Stage

Consequence = dict[Any, Any]
Condition = Callable[[PlayerState], bool] | None


def always_true(_: PlayerState) -> Literal[True]:
    """Return True."""
    return True


@frozen
class Template:
    """Make a template for the messages to be served."""

    text: str = field()
    weight: int = 100

    def format(self, state: PlayerState) -> str:
        """Format the text."""
        return self.text.format(asdict(state))

    def to_embed(self, player: Player, actor: "Actor") -> Embed:
        """Get an embed for UI."""
        # Now you can access actor here
        return Embed(
            title=f"{actor.actor.name} of {player.state.nation_name}",
            description=self.format(player.state),
            color=(0, 0, 255),
        )

    async def ui(self, player: Player, actor: "Actor") -> None:
        await player.ctx.send(embed=self.to_embed(player, actor))


def not_none(var: Any | None) -> Any:  # noqa: ANN401 temporary workaround FIXME
    if var is None:
        raise AttributeError

    return var


@frozen
class ChoiceTemplate(Template):
    choices: dict[str, Consequence] = field(default=None, converter=not_none)  # Specify button color here somehow.
    condition: Condition = always_true

    async def ui(self, player: Player, actor: "Actor") -> None:
        """Send UI and apply consequences."""
        buttons: list[Button] = []

        for id, choice in enumerate(self.choices.items()):
            button = Button(
                label=f"{next(iter(choice.keys()))}",  # Something isn't right here
                style=ButtonStyle.BLURPLE,
                custom_id=f"Choice {id}",
            )
            buttons.append(button)

        embed = self.to_embed(player, actor)

        await player.ctx.send(embed=embed, action_row=ActionRow(*buttons))


total_stages = get_args(Stage)


@frozen
class StageGroup:
    """A helper class to group templates based on their stage in game."""

    stage: Stage | tuple[Stage] | Literal["all"] = field(
        converter=lambda stage: total_stages if stage == "all" else stage,
    )
    templates: list[Template]


@frozen
class ActorData:
    """The data needed to make an embed for UI."""

    name: str
    picture: str  # we'll need to serve these as static content probably


class StageData:
    def __init__(self, templates: list[Template]) -> None:
        self.templates = templates
        self.weights = [template.weight for template in self.templates]

    def get_random(self) -> Template:
        return random.choices(self.templates, weights=self.weights, k=1)[0]  # noqa: S311 Not for cryptographic purposes


class Actor:
    def __init__(self, name: str, picture: str, templates: list[StageGroup]) -> None:
        self.actor = ActorData(name, picture)
        self.stages = self.cast_stages(templates)

    def cast_stages(self, stage_groups: list[StageGroup]) -> dict[Stage, StageData]:  # Not the best code TODO: improve
        stages: dict[Stage, StageData] = {}

        for stage in total_stages:
            stage_templates = []

            for stage_group in stage_groups:
                template_stage = stage_group.stage

                if isinstance(template_stage, int):
                    if template_stage != stage:
                        continue

                elif stage not in template_stage:
                    continue

                stage_templates += stage_group.templates

            stages[stage] = StageData(stage_templates)

        return stages

    async def send(self, target: Player) -> None:
        stage = self.stages[target.game.stage]
        template = stage.get_random()

        await template.ui(target, self)
