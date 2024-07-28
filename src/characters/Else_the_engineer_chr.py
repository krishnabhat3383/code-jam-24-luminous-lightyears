from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t

Actor("Elsa the Engineer", "url_here",[
    StageGroup(1, [
        t(
            "Ruler of {nation_name}, spare some money to design the army's vests!",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        t(
            "The vests are bulletproof! Thanks.",
            choices = {"Great!": {"money": +15}},
            condition = lambda state: state.loyalty>70 and state.money<300,
        ),
    ]),
    StageGroup(2, [
        t("Ruler of {nation_name}, spare some money to design the army's equipment!",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        t(
            "The equipment is top-notch. Thanks.",
            choices = {"Great!": {"money": +30}},
            condition = lambda state: state.loyalty>90 and state.money<600,
        ),
    ]),
    StageGroup(3, [
        t("Ruler of {nation_name}, spare some money to design the army's weapons!",
                 choices = {
                     "Sure": {"money": -40, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        t(
            "The weapons are deadly! Thanks.",
            choices = {"Great!": {"money": +60}},
            condition = lambda state: state.loyalty>110 and state.money<1200,
        ),
    ]),
])
