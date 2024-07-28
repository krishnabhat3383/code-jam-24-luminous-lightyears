"""Dave the doctor character template."""

from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t  # noqa: N813

# fmt: off
character = Actor("Dave the Doctor", "url_here",[
    StageGroup(1, [
        t(
            "Great Leader of {nation_name}, we need funding to create vaccines for this round of seasonal flu!",
            choices={
                "Sure": {"money": -10, "loyalty": +5,  "world_opinion" : +5,  "security" : +5},
                "Flu is easy to ovecome": {"loyalty": -5,  "security" : -10, "world_opinion" : -5},
            },
        ),
        t(
            "We have manufactured the vaccines, but lack the funding to distribute, we require your assistance\
                on this",
            choices = {"Sure": {"money": -15, "Nope":{ "world_opinion" : -20,  "security" : -10,  "loyalty" : -10}}},
        ),
    ]),
    StageGroup(2, [
        t("Great Leader of {nation_name}, we need money to cure an blood borne epidemic !",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5,  "world_opinion" : +10},
                     "Figure it yourself": {"loyalty": -5,  "world_opinion" : -25,  "security" : -20,  "money" : -5},
                 },
            ),
        t(
            "We have cured the epidemic",
            choices = {"Great!": {"money": +30,  "world_opinion" : +10,  "loyalty" : +10}},
            condition = lambda state: state.loyalty>50 and state.money>500,
        ),
    ]),
    StageGroup(3, [
        t("Great Leader of {nation_name}, we need money to cure an blood borne epidemic !",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5,  "world_opinion" : +10},
                     "Figure it yourself": {"loyalty": -5,  "world_opinion" : -25,  "security" : -20,  "money" : -5},
                 },
            ),
        t(
            "We have cured the epidemic",
            choices = {"Great!": {"money": +30,  "world_opinion" : +10,  "loyalty" : +10}},
            condition = lambda state: state.loyalty>50 and state.money>500,
        ),
    ]),
])
