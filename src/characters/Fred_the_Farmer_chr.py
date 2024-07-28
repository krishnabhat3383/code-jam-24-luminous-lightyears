"""Example character template."""

from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t  # noqa: N813

# fmt: off

# fmt: off
character = Actor("Fred the Farmer", "url_here",[
    StageGroup(1, [
        t(
            "Hello, leader of {nation_name}. We request you to give subsidies for seeds",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        t(
            "Thank you for your help, leader!",
            choices = {"It's my duty": {"money": +15}},
            condition = lambda state: state.loyalty>50,
        ),
    ]),
    StageGroup(2, [
        t("Hello, leader of {nation_name}. Can you raise the Minimum Support Price for crops",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +15},
                     "Nope": {"loyalty": -10},
                 },
            ),
        t(
            "Our votes will stay with you",
            choices = {"Thanks!": {"loyalty": +20}},
            condition = lambda state: state.loyalty>70,
        ),
    ]),
    StageGroup(3, [
        t("Hello, leader of {nation_name}. Can you give subsidies for farming equipment?",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +15},
                     "Nope": {"loyalty": -5},
                 },
            ),
        t(
            "We are able to do our work more effectively now",
            choices = {"Great!": {"money": +20}},
        ),
    ]),  
])
