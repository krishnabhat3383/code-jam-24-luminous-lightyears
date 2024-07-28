"""Craig character template."""

from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t  # noqa: N813

# fmt: off
character = Actor("Craig the Contractor", "https://i.postimg.cc/fbbR29cS/Craig.webp",[
    StageGroup(1, [
        t(
            "Leader of {nation_name}, the roads need mending following the heavy use.",
            choices={
                "Sure": {"money": -30, "loyalty": +5,  "world_opinion" : +10,  "security" : +10},
                "Nope": {"loyalty": -5, "world_opinion" : -5},
            },
        ),
        t(
            "The roads are being repaired thanks to the funds provided",
            choices = {
                "Take more funds": {"money": -10,  "loyalty" : +10},
                "Great": {"world_opinion" : +10},
            },
        ),
        t(
            "Some contractors are requesting bonuses for their hard work. Should we approve this?",
            choices={
                "Approve bonuses": {"money": -8, "loyalty": +4},
                "Deny the request": {"loyalty": -3},
            },
            condition=lambda state: state.money > 50,
        ),
    ]),
    StageGroup(2, [
        t("Leader of {nation_name}, we must upgrade our old government buildings.",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5},
                     "Nope": {"loyalty": -5,  "world_opinion" : -10,  "security" : -5},
                 },
            ),
        t(
            "We have shown great strides in the redevelopment plan, would you hold the inaguration ceremony?",
            choices = {"Yes!": {"money": +5, "loyalty":+10,  "world_opinion" : +10},
                       "No!" : { "loyalty" : -5}},
            condition = lambda state: state.loyalty>40,
        ),
        t(
            "We've been asked to build a new hospital in a rural area. Should we take on this project?",
            choices={
                "Yes, build the hospital": {"money": -20, "security": +10, "loyalty": +5},
                "No, it's too expensive": {"security": -5, "loyalty": -3},
            },
        ),
        t(
            "The construction team suggests a new eco-friendly building method. Should we adopt it?",
            choices={
                "Adopt the new method": {"money": -10, "world_opinion": +10},
                "Stick to old methods": {"world_opinion": -5},
            },
            condition=lambda state: state.world_opinion > 50,
        ),
    ]),
    StageGroup(3, [
        t("Leader of {nation_name}, the drains need to be declogged following the flood.",
                 choices = {
                     "Sure": {"money": -40, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        t(
            "The international community is considering us for a prestigious construction award. Should we lobby for it?",  # noqa: E501
            choices={
                "Yes, lobby for the award": {"money": -10, "world_opinion": +15, "loyalty": +5},
                "No, it's not worth it": {"world_opinion": -5},
            },
        ),
        t(
            "Several community leaders are asking for funds to improve local infrastructure. Should we approve it?",
            choices={
                "Approve the funds": {"money": -20, "security": +10},
                "No, we can't afford it": {"security": -5},
            },
            condition=lambda state: state.money > 100,
        ),
    ]),
], weight=70)
