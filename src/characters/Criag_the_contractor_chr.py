from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t

character = Actor("Craig the Contractor", "url_here",[
    StageGroup(1, [
        t(
            "Ruler of {nation_name}, the roads need mending following the earthquake.",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        t(
            "",
            choices = {"Great!": {"money": +15}},
            condition = lambda state: state.loyalty>70 and state.money<300,
        ),
    ]),
    StageGroup(2, [
        t("Ruler of {nation_name}, the houses need patching following the tornado.",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        t(
            "Great! Looks like a tornado never hit this place.",
            choices = {"Great!": {"money": +30}},
            condition = lambda state: state.loyalty>90 and state.money<600,
        ),
    ]),
    StageGroup(3, [
        t("Ruler of {nation_name}, the drains need to be declogged following the flood.",
                 choices = {
                     "Sure": {"money": -40, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        t(
            "Great! Looks like a flood never hit this place.",
            choices = {"Great!": {"money": +60}},
            condition = lambda state: state.loyalty>110 and state.money<1200,
        ),
    ]),
])

