from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t

# fmt: off
character = Actor("John the Farmer", "url_here",[
    StageGroup(1, [
        t(
            "Hello, leader of {nation_name}. Can you spare some money for our new farming equipment?",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        t(
            "Things are great, we managed to grow even more crops than expected.\
                Thank you for your help, leader! \n Here, have this small gift from our community",
            choices = {"Thanks!": {"money": +15}},
            condition = lambda state: state.loyalty>70 and state.money<300,
        ),
    ]),
    StageGroup(2, [
        t("O Great leader of {nation_name}! Please provide money to upgrade our equipment",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        t(
            "Things are great, we managed to grow even more crops than expected.\
                Thank you for your help, leader! \n Here, have this small gift from our community",
            choices = {"Thanks!": {"money": +30}},
            condition = lambda state: state.loyalty>75 and state.money<800,
        ),
    ]),
])
