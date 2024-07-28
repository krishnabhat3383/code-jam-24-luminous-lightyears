from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t

character = Actor("Andy the Athlete", "url_here",[
    StageGroup(1, [
        t(
            "Dear leader of {nation_name}, please help our climate change marathon's fundraiser.",
            choices={
                "Sure": {"money": -10, "loyalty": +5, "world_opinion" : +10},
                "Nope": {"loyalty": -5},
            },
        ),
        t(
            "The marathon was phenomenal! Thanks for your support.",
            choices = {"Great!": {"money": +15}},
            condition = lambda state: state.loyalty>70 and state.money<300,
        ),
    ]),
    StageGroup(2, [
        t("Dear leader of {nation_name}, please help our climate change marathon's fundraiser.",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        t(
            "The marathon was phenomenal! Thanks for your support.",
            choices = {"Great!": {"money": +30}},
            condition = lambda state: state.loyalty>90 and state.money<600,
        ),
    ]),
    StageGroup(3, [
        t("Dear leader of {nation_name}, please help our climate change marathon's fundraiser.",
                 choices = {
                     "Sure": {"money": -40, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        t(
            "The marathon was phenomenal! Thanks for your support.",
            choices = {"Great!": {"money": +60}},
            condition = lambda state: state.loyalty>110 and state.money<1200,
        ),
    ]),
])

