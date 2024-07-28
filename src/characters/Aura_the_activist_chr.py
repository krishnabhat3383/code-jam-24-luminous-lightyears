from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t

character = Actor("Aura the Activist", "url_here",[
    StageGroup(1, [
        t(
            "Kind leader of {nation_name}! Please donate to our LGBTQ+ movement.",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        t(
            "Rights are Rights! You did the right thing.",
            choices = {"Great!": {"money": +15}},
            condition = lambda state: state.loyalty>70 and state.money<300,
        ),
    ]),
    StageGroup(2, [
        t("Kind leader of {nation_name}! Please donate to our LGBTQ+ movement.",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        t(
            "Rights are Rights! You did the right thing.",
            choices = {"Great!": {"money": +30}},
            condition = lambda state: state.loyalty>90 and state.money<600,
        ),
    ]),
    StageGroup(3, [
        t("Kind leader of {nation_name}! Please donate to our LGBTQ+ movement.",
                 choices = {
                     "Sure": {"money": -40, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        t(
            "Rights are Rights! You did the right thing.",
            choices = {"Great!": {"money": +60}},
            condition = lambda state: state.loyalty>110 and state.money<1200,
        ),
    ]),
])

