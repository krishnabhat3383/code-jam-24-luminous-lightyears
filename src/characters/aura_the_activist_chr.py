"""Aura character template."""

from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t  # noqa: N813

# fmt: off
character = Actor("Aura the Activist", "https://i.postimg.cc/qvw7xL3d/aura.jpg",[
    StageGroup(1, [
        t(
            "Kind leader of {nation_name}! Please donate to our LGBTQ+ movement.",
            choices={
                "Sure": {"money": -10, "loyalty": +5, "world_opinion" : +10},
                "Nope": {"loyalty": -5,  "world_opinion" : -15},
            },
        ),
        t(
            "Rights are Rights! You did the right thing.",
            choices = {"Great!": {"money": +5}},
            condition = lambda state: state.loyalty>30,
        ),
        t(
            "There's an opportunity to host a human rights seminar in our nation. Should we do it?",
            choices={
                "Yes, host the seminar": {"money": -8, "world_opinion": +5, "loyalty": +3},
                "No, it's too costly": {"loyalty": -3, "world_opinion": -2},
            },
        ),
    ]),
    StageGroup(2, [
        t(
            "One of our leading activists has been unjustly detained. Should we fund their legal defense?",
            choices={
                "Yes, fund legal defense": {"money": -10, "loyalty": +10},
                "No, it's too costly": {"loyalty": -10},
            },
        ),
        t(
            "The environmental group is requesting funds to plant trees across the city. Should we approve this?",
            choices={
                "Approve funds": {"money": -8, "loyalty": +5, "world_opinion": +3},
                "Deny the request": {"loyalty": -4},
            },
            condition=lambda state: state.loyalty > 60,
        ),
        t(
            "News in someone gassed the rally.",
            choices = {"Great!": {"money": -10,  "world_opinion" : -10,  "security" : -5}},
            condition = lambda state: state.loyalty<50 and state.security<75,
        ),
    ]),
    StageGroup(3, [
        t(
            "The international community is considering us for a prestigious human rights award. Should we lobby for it?",  # noqa: E501
            choices={
                "Yes, lobby for the award": {"money": -10, "world_opinion": +15, "loyalty": +5},
                "No, it's not worth it": {"world_opinion": -5},
            },
        ),
        t(
            "Several community leaders are asking for funds to improve local social programs. Should we approve it?",
            choices={
                "Approve the funds": {"money": -20, "loyalty": +10},
                "No, we can't afford it": {"loyalty": -5},
            },
            condition=lambda state: state.money > 100,
        ),
        t(
            "There's a push to create stricter environmental regulations. Should we support it?",
            choices={
                "Yes, support the regulations": {"security": +5, "world_opinion": +10},
                "No, it's too restrictive": {"loyalty": -5, "world_opinion": -5},
            },
            condition=lambda state: state.security > 50,
        ),
    ]),
], weight=90)
