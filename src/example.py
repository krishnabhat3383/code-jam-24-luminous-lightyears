from models import Actor, StageGroup, Template

# fmt: off
Actor("John the Farmer", "url_here",[
    StageGroup(1, [
        Template(
            "Hello, leader of {nation_name}. Can you spare some money for our new farming equipment?",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        Template(
            "Things are great, we managed to grow even more crops than expected.\
                Thank you for your help, leader! \n Here, have this small gift from our community",
            choices = {"Thanks!": {"money": +15}},
            condition = lambda state: state.loyalty>70 and state.money<300,
        ),
    ]),
    StageGroup(2, [
        Template("O Great leader of {nation_name}! Please provide money to upgrade our equipment",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "Things are great, we managed to grow even more crops than expected.\
                Thank you for your help, leader! \n Here, have this small gift from our community",
            choices = {"Thanks!": {"money": +30}},
            condition = lambda state: state.loyalty>75 and state.money<800,
        ),
    ]),
])
