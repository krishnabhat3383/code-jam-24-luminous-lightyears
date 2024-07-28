"""General template and information."""

from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t  # noqa: N813

# fmt: off
character = Actor("Gary the General", "https://i.postimg.cc/c134bZnh/gary.webp",[
    StageGroup(1, [
        t(
            "Sir, ruler of {nation_name}! The army needs new helmets to improve safety!",
            choices={
                "Sure": {"money": -10, "loyalty": +5, "security": +3},
                "Nope": {"loyalty": -5, "security": -5},
            },
            weight=90,
        ),
        t(
            "Sir, ruler of {nation_name}! The army needs new vests to improve safety!",
            choices={
                "Sure": {"money": -5, "loyalty": +3, "security": +2},
                "Nope": {"loyalty": -3, "security": -2},
            },
            weight=110,
        ),
        t(
            "Sir, we have received intelligence about potential threats from neighboring countries.",
            choices={
                "Increase border security": {"money": -20, "security": +10, "world_opinion": -5, "loyalty": +3},
                "Ignore the threats": {"security": -10, "world_opinion": +5, "loyalty": -5},
            },
            weight=80,
        ),
        t(
            "Good morning, {nation_name}! Our brave soldiers are out training hard today. 💪 #MilitaryStrength #ProudNation",  # noqa: E501
            choices={
                "Like": {"loyalty": +2},
                "Share": {"world_opinion": +1},
                "Ignore": {"loyalty": -2},
            },
            weight=80,
        ),
        t(
            "Just received new supplies for the troops. Thanks to everyone for your support! 🛡️ #SupportOurTroops #NationalSecurity",  # noqa: E501
            choices={
                "Comment 'Great job!'": {"loyalty": +3},
                "Ignore": {"loyalty": -3},
            },
            weight=120,
        ),
    ]),
    StageGroup(2, [
        t(
            "Sir, ruler of {nation_name}! The army needs equipment Sir!",
            choices = {
                "Sure": {"money": -20, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
            weight=150,
        ),
        t(
            "Thanks Sir! Now our army is stronger than ever Sir!",
            choices = {"Great!": {"money": +30}},
            condition = lambda state: state.security>80 and state.money<200 and state.loyalty>70,
            weight=150,
        ),
        t(
            "Sir, we've been invited to a joint military exercise with allied nations.",
            choices={
                "Participate in the exercise": {"money": -25, "security": +10, "world_opinion": +7},
                "Decline the invitation": {"world_opinion": -5, "security": -3},
            },
            condition = lambda state: state.security>60 and state.money>120,
            weight=80,
        ),
        t(
            "Our intelligence team has thwarted a potential threat. Kudos to them! 🕵️‍♂️ #SecurityFirst #StaySafe",
            choices={
                "Like": {"security": +2},
                "Share": {"world_opinion": +2},
                "Ignore": {"loyalty": -5},
            },
        ),
    ]),
    StageGroup(3, [
        t(
            "Sir, our intelligence agency needs more resources to counter espionage.",
            choices={
                "Allocate resources": {"money": -40, "security": +12, "loyalty": +5},
                "Deny the request": {"loyalty": -10, "security": -5},
            },
            weight=90,
        ),
        t(
            "Sir, ruler of {nation_name}! The army needs weapons Sir!",
            choices = {
                "Sure": {"money": -40, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
            weight=150,
        ),
        t(
            "Sir, a major international summit on global security is approaching. Should we attend?",
            choices={
                "Attend the summit": {"money": -35, "world_opinion": +15, "security": +5},
                "Skip the summit": {"world_opinion": -10, "security": -2},
            },
            weight=105,
        ),
        t(
            "Proud to announce new advancements in our military technology. Future-ready and strong! 🚀 #TechInDefense #Innovation",  # noqa: E501
            choices={
                "Like": {"security": +3},
                "Comment 'Impressive!'": {"world_opinion": +3},
                "Ignore": {"loyalty": -5, "world_opinion": -10},
            },
            weight=120,
        ),
        t(
            "Remembering our fallen heroes today. Their sacrifice keeps us free. #RemembranceDay #NeverForget",
            choices={
                "Like": {"loyalty": +3},
                "Share": {"world_opinion": +2},
                "Ignore": {"loyalty": -5, "world_opinion": -10},
            },
            weight=150,
        ),
    ]),
], weight=130)
