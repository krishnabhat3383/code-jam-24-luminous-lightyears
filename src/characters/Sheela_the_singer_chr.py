from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t

Actor("Sheela the Singer", "url_here",[
    StageGroup(1, [
        t(
            "Blessed leader of {nation_name}, please fund my public concert!",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        t(
            "The concert was on fire! Thank you so much.",
            choices = {"Great!": {"money": +15}},
            condition = lambda state: state.loyalty>70 and state.money<300,
        ),
    ]),
    StageGroup(2, [
        t("Blessed leader of {nation_name}, please fund my public concert!",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        t(
            "The concert was on firee! Thank you so much.",
            choices = {"Great!": {"money": +30}},
            condition = lambda state: state.loyalty>90 and state.money<600,
        ),
    ]),
    StageGroup(3, [
        t("Blessed leader of {nation_name}, please fund my public concert!",
                 choices = {
                     "Sure": {"money": -40, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        t(
            "The concert was on fireee! Thank you so much.",
            choices = {"Great!": {"money": +60}},
            condition = lambda state: state.loyalty>110 and state.money<1200,
        ),
    ]),
])

