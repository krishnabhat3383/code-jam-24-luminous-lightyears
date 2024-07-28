"""Else character template."""

from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t  # noqa: N813

# fmt: off
character = Actor("Elsa the Engineer", "https://i.postimg.cc/kGWJ6Fmz/elsa.webp",[
    StageGroup(1, [
        t(
            "Leader of {nation_name},it is my humble request allocate more budget towards research for\
                technology used in military field",
            choices={
                "Sure": {"money": -30, "loyalty": +5,  "security" : +15},
                "Nope": {"loyalty": -5, "world_opinion" : -10},
            },
        ),
        t(
            "We are competiting the cutting edge military tech now.",
            choices = {"Great!": {"security": +10}},
            condition = lambda state: state.security<50,
        ),
    ]),
    StageGroup(2, [
        t("Leader of {nation_name}, it is my humble request allocate some of the budget\
           in the manufacturing sector",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5, "world_opinion" : +10},
                     "Nope": {"loyalty": -5, "money" : -10},
                 },
            ),
        t(
            "Now we won't be requiring to be import certain important materials.",
            choices = {"Great!": {"money": +30}},
            condition = lambda state: state.loyalty>40 and state.money>500,
        ),
    ]),
    StageGroup(3, [
        t("Leader of {nation_name}, it is my humble request to give subsidies for \
          research companies in our nation",
                 choices = {
                     "Sure": {"money": -30, "loyalty": +5 , "world_opinion" : +10},
                     "Nope": {"loyalty": -5 , "world_opinion" : -10},
                 },
            ),
        t(
            "Now the nation would be filing more patents.",
            choices = {"Great!": {"money": +50}},
            condition = lambda state: state.security>50 and state.money>500,
        ),
    ]),
], weight=60)
