"""Dave the doctor character template."""

from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t  # noqa: N813

# fmt: off
character = Actor("Dave the Doctor", "https://i.postimg.cc/Y9GqkByp/Dave.webp",[
    StageGroup(1, [
        t(
            "Great Leader of {nation_name}, we need funding to create vaccines for this round of seasonal flu!",
            choices={
                "Sure": {"money": -10, "loyalty": +5,  "world_opinion" : +5,  "security" : +5},
                "Flu is easy to ovecome": {"loyalty": -5,  "security" : -10, "world_opinion" : -5},
            },
        ),
        t(
            "We have manufactured the vaccines, but lack the funding to distribute, we require your assistance on this",  # noqa: E501
            choices = {
                "Sure": {"money": -15},
                "Nope":{ "world_opinion" : -20,  "security" : -10,  "loyalty" : -10},
            },
        ),
        t(
            "Leader of {nation_name}, our hospital is overwhelmed with patients. We need additional funding to hire more staff.",  # noqa: E501
            choices={
                "Approve funding": {"money": -20, "security": +5, "loyalty": +3},
                "Deny funding": {"security": -5, "loyalty": -3},
            },
        ),
        t(
            "There's a flu outbreak in the neighboring regions. Should we prepare by stocking up on vaccines?",
            choices={
                "Yes, stock up on vaccines": {"money": -10, "security": +10, "world_opinion": +5},
                "No, it's not necessary": {"security": -5, "world_opinion": -3},
            },
        ),
        t(
            "Some doctors are requesting additional training to improve their skills. Should we invest in their education?",  # noqa: E501
            choices={
                "Invest in training": {"money": -10, "loyalty": +3, "security": +2},
                "No, they are skilled enough": {"loyalty": -2, "security": -1},
            },
            condition=lambda state: state.money > 30,
        ),
    ]),
    StageGroup(2, [
        t(
            "There's a proposal to build a new children's hospital in a underserved area. Should we support it?",
            choices={
                "Yes, build the hospital": {"money": -25, "loyalty": +10, "world_opinion": +5},
                "No, we can't afford it": {"loyalty": -5, "world_opinion": -3},
            },
        ),
        t(
            "We have the opportunity to participate in a global health initiative. Should we join?",
            choices={
                "Yes, join the initiative": {"money": -15, "world_opinion": +15, "security": +5},
                "No, it's too costly": {"world_opinion": -5, "security": -3},
            },
            condition=lambda state: state.world_opinion > 40,
        ),
        t(
            "We've been offered a partnership with a leading medical research facility. Should we accept?",
            choices={
                "Yes, accept the partnership": {"money": -20, "world_opinion": +10, "security": +5},
                "No, we can manage on our own": {"world_opinion": -5, "security": -3},
            },
        ),
    ]),
    StageGroup(3, [
        t(
            "We have the chance to lead a groundbreaking health research project. Should we take the lead?",
            choices={
                "Lead the project": {"money": -30, "world_opinion": +15, "security": +10},
                "No, let others lead": {"world_opinion": -5, "security": -3},
            },
            condition=lambda state: state.security > 50,
        ),
        t(
            "A leading pharmaceutical company wants to conduct trials in our nation. Should we allow it?",
            choices={
                "Allow the trials": {"money": +20, "security": +5, "world_opinion": +5},
                "Deny the trials": {"security": -5, "world_opinion": -5},
            },
            condition=lambda state: state.money < 50,
        ),
        t(
            "The community is requesting free health check-ups. Should we organize this?",
            choices={
                "Yes, organize free check-ups": {"money": -15, "loyalty": +10, "world_opinion": +5},
                "No, it's too costly": {"loyalty": -5, "world_opinion": -3},
            },
            condition=lambda state: state.loyalty > 50,
        ),
    ]),
], weight=110)
