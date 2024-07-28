"""Sheel template information."""

from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t  # noqa: N813

# fmt: off
character = Actor("Sheela the Singer", "https://i.postimg.cc/RZSShHbp/sheela.webp",[
    StageGroup(1, [
        t(
            "Blessed leader of {nation_name}, please fund my public concert!",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        t(
            "Leader of {nation_name}, I need funding to produce a new national anthem that will boost our citizens' morale.",  # noqa: E501
            choices={
                "Approve funding": {"money": -10, "loyalty": +5},
                "Deny funding": {"loyalty": -5},
            },
        ),
    ]),
    StageGroup(2, [
        t(
            "I want to start a music school to nurture local talent. It will need substantial investment.",
            choices={
                "Approve the school": {"money": -25, "loyalty": +15, "world_opinion": +5},
                "Deny the project": {"loyalty": -10},
            },
        ),
        t(
            "Excited to be a guest on the popular TV show this week. Tune in! 📺🎤 #TVAppearance #Excited",
            choices={
                "Like": {"world_opinion": +2},
                "Share": {"world_opinion": +3},
                "Ignore": {},
            },
        ),
    ]),
    StageGroup(3, [
        t(
            "I've been nominated for an international music award! Thank you for all your support. 🌟🎶 #MusicAward #FeelingBlessed",  # noqa: E501
            choices={
                "Like": {"loyalty": +3},
                "Share": {"world_opinion": +3},
                "Ignore": {},
            },
            condition=lambda state: state.world_opinion > 50,
        ),
        t(
            "Dreaming big! Planning to start a music school to nurture young talent. 🎼🎓 #MusicSchool #FutureTalent",
            choices={
                "Like": {"loyalty": +3},
                "Share": {"world_opinion": +3},
                "Ignore": {},
            },
        ),
    ]),
])
