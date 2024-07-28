from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t

character = Actor("Sam the Scientist", "url_here",[
    StageGroup(1, [
        t(
            "Greetings, esteemed leader of {nation_name}. May I request your consideration for a financial contribution\
                towards our research?",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        t(
            "Alzhemier's will be cured soon! Thanks for your contribution",
            choices = {"Great!": {"money": +15}},
            condition = lambda state: state.loyalty>70 and state.money<300,
        ),
    ]),
    StageGroup(2, [
        t("Greetings, esteemed leader of {nation_name}. May I request your consideration for a financial contribution\
                towards our research?",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        t(
            "Parkinson's will be cured soon! Thanks for your contribution",
            choices = {"Great!": {"money": +30}},
            condition = lambda state: state.loyalty>90 and state.money<600,
        ),
    ]),
    StageGroup(3, [
        t("Greetings, esteemed leader of {nation_name}. May I request your consideration for a financial contribution\
                towards our research?",
                 choices = {
                     "Sure": {"money": -40, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        t(
            "AIDS will be cured soon! Thanks for your contribution",
            choices = {"Great!": {"money": +60}},
            condition = lambda state: state.loyalty>110 and state.money<1200,
        ),
    ]),
])

