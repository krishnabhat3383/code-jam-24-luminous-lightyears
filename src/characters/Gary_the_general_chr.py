from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t

character = Actor("Gary the General", "url_here",[
    StageGroup(1, [
        t(
            "Sir, ruler of {nation_name}! The army needs vests Sir!",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        t(
            "Thanks Sir! Now our army is stronger than ever Sir!",
            choices = {"Great!": {"money": +15}},
            condition = lambda state: state.loyalty>70 and state.money<300,
        ),
    ]),
    StageGroup(2, [
        t("Sir, ruler of {nation_name}! The army needs equipment Sir!",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        t(
            "Thanks Sir! Now our army is stronger than ever Sir!",
            choices = {"Great!": {"money": +30}},
            condition = lambda state: state.loyalty>90 and state.money<600,
        ),
    ]),
    StageGroup(3, [
        t("Sir, ruler of {nation_name}! The army needs weapons Sir!",
                 choices = {
                     "Sure": {"money": -40, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        t(
            "Thanks Sir! Now our army is stronger than ever Sir!",
            choices = {"Great!": {"money": +60}},
            condition = lambda state: state.loyalty>110 and state.money<1200,
        ),
    ]),
])

