from collections.abc import Callable
from typing import Any, Literal, get_args

from attrs import asdict, define, field, frozen
from interactions.models.discord.embed import Embed

Stage = Literal[1, 2, 3]  # Adjustable


@define
class State:
    nation_name: str
    stage: Stage = 1

    # Money with the government 
    money: float = 100
    
    # How loyal people feel to the current government that you have created
    loyalty: float = 50
    
    # How vulnerable is the country from external threats  
    security: float = 50
    
    # Lower means entity sabotage and vice versa (might add this as a later future)
    world_opinion: float = 50 

    def apply(self, consequence: dict) -> None:
        for k, v in consequence.items():
            self.__dict__[k] += v


# Consequence = Callable[[State], None]
Consequence = dict[Any, Any]
Condition = Callable[[State], bool] | None


@frozen
class Template:
    @staticmethod
    def convert_condition(condition: Condition | None) -> Condition:
        def always_true(_: State) -> True:
            return True

        if condition is None:
            return always_true

        return condition

    string: str
    choices: dict[None, Consequence]
    condition: Condition = field(converter=convert_condition)

    def format(self, state: State) -> str:
        return self.string.format(asdict(state))

    def to_embed(self, state: State) -> Embed:
        raise NotImplementedError


# StageSpec = Stage | tuple[Stage] | Literal["all"]
TotalStages = get_args(Stage)


@frozen
class StageGroup:
    # @staticmethod
    # def convert_stage(stage: StageSpec) -> Stage | tuple[Stage]:
    #     if stage == "all":
    #         return TotalStages

    #     return stage

    stage: Stage | tuple[Stage] | Literal["all"] = field(
        converter=lambda stage: TotalStages if stage == "all" else stage,
    )
    templates: list[Template]


@frozen
class Actor:
    name: str
    picture: str  # we'll need to serve these as static content probably
    templates: list[StageGroup]
