"""Fred character template."""

from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t  # noqa: N813

# fmt: off
character = Actor("Fred the Farmer", "https://i.postimg.cc/ZKcmGqK8/Fred.webp",[
    StageGroup(1, [
        t(
            "Hello, leader of {nation_name}. We request you to give subsidies for seeds",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        t(
            "Leader of {nation_name}, our farms need new irrigation systems to increase crop yield.",
            choices={
                "Approve funding": {"money": -15, "security": +5, "loyalty": +3},
                "Deny funding": {"security": -5, "loyalty": -3},
            },
        ),
        t(
            "There's an opportunity to switch to organic farming. Should we support this transition?",
            choices={
                "Yes, support organic farming": {"money": -10, "world_opinion": +10, "loyalty": +5},
                "No, it's not necessary": {"world_opinion": -5, "loyalty": -3},
            },
        ),
        t(
            "Farmers are requesting subsidies to cope with recent droughts. Should we grant them?",
            choices={
                "Grant subsidies": {"money": -15, "loyalty": +5, "world_opinion": +3},
                "No, we can't afford it": {"loyalty": -5, "world_opinion": -3},
            },
            condition=lambda state: state.money > 30,
        ),
    ]),
    StageGroup(2, [
        t("Hello, leader of {nation_name}. Can you raise the Minimum Support Price for crops",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +15},
                     "Nope": {"loyalty": -10},
                 },
            ),
        t(
            "There's a proposal to introduce advanced farming technologies. Should we invest in this?",
            choices={
                "Yes, invest in technology": {"money": -20, "security": +10, "loyalty": +5},
                "No, it's too expensive": {"security": -5, "loyalty": -3},
            },
        ),
        t(
            "A neighboring country wants to collaborate on a farming project. Should we join them?",
            choices={
                "Yes, join the project": {"money": -15, "world_opinion": +10, "security": +5},
                "No, we can manage on our own": {"world_opinion": -5, "security": -3},
            },
        ),
        t(
            "Farmers are organizing a festival to celebrate the harvest. Should we sponsor it?",
            choices={
                "Sponsor the festival": {"money": -10, "loyalty": +10, "world_opinion": +5},
                "No, it's not necessary": {"loyalty": -5, "world_opinion": -3},
            },
            condition=lambda state: state.world_opinion > 40,
        ),
    ]),
    StageGroup(3, [
        t(
            "Our nation is being considered for a prestigious agricultural award. Should we lobby for it?",
            choices={
                "Yes, lobby for the award": {"money": -10, "world_opinion": +20, "loyalty": +5},
                "No, it's not worth it": {"world_opinion": -5},
            },
        ),
        t(
            "We have the chance to lead a global agricultural research project. Should we take the lead?",
            choices={
                "Lead the project": {"money": -25, "world_opinion": +15, "security": +10},
                "No, let others lead": {"world_opinion": -5, "security": -3},
            },
            condition=lambda state: state.security > 50,
        ),
        t(
            "A major agricultural firm wants to test new fertilizers in our fields. Should we allow it?",
            choices={
                "Allow the tests": {"money": +20, "security": +5, "world_opinion": +5},
                "Deny the tests": {"security": -5, "world_opinion": -5},
            },
            condition=lambda state: state.money < 50,
        ),
        t(
            "Farmers are requesting financial aid due to a recent pest infestation. Should we help them?",
            choices={
                "Yes, provide aid": {"money": -15, "loyalty": +10, "world_opinion": +5},
                "No, it's too costly": {"loyalty": -5, "world_opinion": -3},
            },
            condition=lambda state: state.loyalty > 50,
        ),
    ]),
], weight=120)
