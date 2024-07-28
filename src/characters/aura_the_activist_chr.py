"""Aura character template."""

from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t  # noqa: N813

# fmt: off
character = Actor("Aura the Activist", "url_here",[
    StageGroup(1, [
        t(
            "Kind leader of {nation_name}! Please donate to our LGBTQ+ movement.",
            choices={
                "Sure": {"money": -10, "loyalty": +5, "world_opinion" : +10},
                "Nope": {"loyalty": -5,  "world_opinion" : -15},
            },
        ),
        t(
            "Rights are Rights! You did the right thing.",
            choices = {"Great!": {"money": +5}},
            condition = lambda state: state.loyalty>30,
        ),
    ]),
    StageGroup(2, [
        t("Kind leader of {nation_name}! Please donate to our LGBTQ+ movement.",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5,  "world_opinion" : +10},
                     "Nope": {"loyalty": -5,  "world_opinion" : -10},
                 },
            ),
        t(
            "Rights are Rights! You did the right thing.",
            choices = {"Great!": {"money": +5}},
            condition = lambda state: state.loyalty>40,
        ),
        t(
            "News in someone gassed the rally.",
            choices = {"Great!": {"money": -10,  "world_opinion" : -10,  "security" : -5}},
            condition = lambda state: state.loyalty<50 and state.security<75,
        ),
    ]),
    StageGroup(3, [
        t("Kind leader of {nation_name}! Please donate to our LGBTQ+ movement.",
                 choices = {
                     "Sure": {"money": -40, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        t(
            "Rights are Rights! You did the right thing.",
            choices = {"Great!": {"money": +60}},
            condition = lambda state: state.loyalty>20 and state.money<100,
        ),
        t(
            "News in someone gassed the rally.",
            choices = {"Great!": {"money": -10,  "world_opinion" : -10,  "security" : -5}},
            condition = lambda state: state.loyalty<90 and state.security<100,
        ),
    ]),
])
