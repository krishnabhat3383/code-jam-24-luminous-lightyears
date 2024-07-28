from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t

Actor("Sandra the Spy", "url_here",[
    StageGroup(1, [
        t(
            "ruler of {nation_name}, spy squad needs supplies",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        t(
            "The supplies helped our mission",
            choices = {"Great!": {"money": +15}},
            condition = lambda state: state.loyalty>70 and state.money<300,
        ),
    ]),
    StageGroup(2, [
        t("ruler of {nation_name}, spy squad needs supplies",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        t(
            "The supplies helped our mission",
            choices = {"Great!": {"money": +30}},
            condition = lambda state: state.loyalty>90 and state.money<600,
        ),
    ]),
])

