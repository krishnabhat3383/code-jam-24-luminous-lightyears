"""Andy character template."""

from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t  # noqa: N813

# fmt: off
character = Actor("Andy the Athlete", "url_here",[
    StageGroup(1, [
        t(
            "Dear leader of {nation_name}, please help our climate change marathon's fundraiser.",
            choices={
                "Sure": {"money": -10, "loyalty": +5, "world_opinion" : +10},
                "Nope": {"loyalty": -5, "world_opinion":-5},
            },
        ),
        t(
            "The marathon was phenomenal! Thanks for your support.",
            choices = {"Great!": {"money": +15, "loyalty":+10}},
            condition = lambda state: state.money<150,
        ),
    ]),
    StageGroup(2, [
        t("Dear leader of {nation_name}, please help our climate change marathon's fundraiser.",
                 choices = {
                     "Sure": {"money": -15, "loyalty": +10, "world_opinion" : +10},
                     "Nope": {"loyalty": -5, "world_opinion":-10},
                 },
            ),
        t(
            "The marathon was phenomenal! Thanks for your support.",
            choices = {"Great!": {"money": +20}},
            condition = lambda state: state.loyalty>20 and state.money<250,
        ),
    ]),
    StageGroup(3, [
        t("Dear leader of {nation_name}, please help our climate change marathon's fundraiser.",
                 choices = {
                     "Sure": {"money": -45, "loyalty": +5, "world_opinion" : +10},
                     "Nope": {"loyalty": -5, "world_opinion":-5},
                 },
            ),
        t(
            "The marathon was good, but several people were hospitalised due to heatstroke.",
            choices = {"Oh no!": {"money": +30, "world_opinion" : -5}},
            condition = lambda state: state.loyalty>30 and state.money<300,
        ),
        t(
            "The marathon went viral, and we were able to raise a lot of funds.",
            choices = {"Awesome!": {"money": +70, "world_opinion" : +10}},
            condition = lambda state: state.loyalty>50 and state.money<200,
        ),
    ]),
])
