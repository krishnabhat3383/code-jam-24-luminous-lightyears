"""Wong the worker template information."""

from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t  # noqa: N813

# fmt: off
character = Actor("Wong the Worker", "https://i.postimg.cc/ht2SdtkD/wong.webp",[
    StageGroup(1, [
        t(
            "O great leader of {nation_name}. May thou be kind enough to raise our minimum wage",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        t(
            "Leader of {nation_name}, our factory needs new machinery to increase production.",
            choices={
                "Approve funding": {"money": -15, "loyalty": +5},
                "Deny funding": {"loyalty": -5},
            },
        ),
        t(
            "We need better safety equipment for our workers. Can you help?",
            choices={
                "Provide equipment": {"money": -10, "security": +5, "loyalty": +5},
                "Deny request": {"loyalty": -5, "security": -5},
            },
        ),
        t(
            "Excited to announce we'll be at the local job fair. Come and join our team! 👷‍♀️📈 #JobFair #HiringNow",
            choices={
                "Like": {"loyalty": +2},
                "Share": {"loyalty": +3},
                "Ignore": {},
            },
        ),
    ]),
    StageGroup(2, [
        t(
            "A nearby country is interested in a trade agreement. Should we pursue it?",
            choices={
                "Yes, pursue agreement": {"money": +10, "world_opinion": +5},
                "No, it's not worth it": {"world_opinion": -5},
            },
            condition=lambda state: state.world_opinion > 30,
        ),
        t(
            "We've had a surge in production. Should we give bonuses to the workers?",
            choices={
                "Yes, give bonuses": {"money": -15, "loyalty": +10},
                "No, save the money": {"loyalty": -5},
            },
        ),
        t(
            "Welcoming foreign investment to boost our production capabilities. 🌍💼 #Investment #Growth",
            choices={
                "Like": {"world_opinion": +2},
                "Share": {"world_opinion": +3},
                "Ignore": {},
            },
        ),
    ]),
    StageGroup(3, [
        t(
            "Our competitors are starting to outpace us. Should we invest in cutting-edge technology?",
            choices={
                "Yes, invest": {"money": -30, "security": +10, "loyalty": +5},
                "No, stick with what we have": {"loyalty": -5},
            },
        ),
        t(
            "We've been approached by a foreign investor. Should we accept their investment?",
            choices={
                "Yes, accept": {"money": +25, "world_opinion": +10},
                "No, decline": {"world_opinion": -5},
            },
        ),
        t(
            "There's a growing unrest among workers due to long hours. Should we reduce working hours?",
            choices={
                "Yes, reduce hours": {"money": -10, "loyalty": +10, "security": +5},
                "No, keep the hours": {"loyalty": -10, "security": -5},
            },
        ),
        t(
            "We've developed a new product. Should we launch it internationally?",
            choices={
                "Yes, launch internationally": {"money": -20, "world_opinion": +15},
                "No, focus locally": {"world_opinion": -5},
            },
        ),
        t(
            "A new labor union is forming. Should we support its formation?",
            choices={
                "Yes, support it": {"loyalty": +15, "security": +5},
                "No, oppose it": {"loyalty": -10, "security": -5},
            },
        ),
        t(
            "Launching our new product internationally! Exciting times ahead. 🌍🚀 #NewProduct #GlobalLaunch",
            choices={
                "Like": {"world_opinion": +3},
                "Share": {"world_opinion": +4},
                "Ignore": {},
            },
        ),
    ]),
], weight=110)
