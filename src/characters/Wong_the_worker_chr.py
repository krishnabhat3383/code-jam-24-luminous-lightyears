from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t

character = Actor("Wong the Worker", "url_here",[
    StageGroup(1, [
        t(
            "O great leader of {nation_name}. May thou be kind enough to raise our minimum wage",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        t(
            "Thank you! We have been extremely productive and produced so much more goods.",
            choices = {"Great!": {"money": +15}},
            condition = lambda state: state.loyalty>70 and state.money<300,
        ),
    ]),
    StageGroup(2, [
        t("O great leader of {nation_name}. May thou be kind enough to raise our minimum wage",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        t(
            "Thank you! We have been extremely productive and produced so much more goods.",
            choices = {"Great!": {"money": +30}},
            condition = lambda state: state.loyalty>90 and state.money<600,
        ),
    ]),
    StageGroup(3, [
        t("O great leader of {nation_name}. May thou be kind enough to raise our minimum wage",
                 choices = {
                     "Sure": {"money": -40, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        t(
            "Thank you! We have been extremely productive and produced so much more goods.",
            choices = {"Great!": {"money": +60}},
            condition = lambda state: state.loyalty>110 and state.money<1200,
        ),
    ]),
])

