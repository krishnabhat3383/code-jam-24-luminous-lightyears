"""Andy character template."""

from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t  # noqa: N813

# fmt: off
character = Actor("Andy the Athlete", "https://i.postimg.cc/50h92KZ8/Andy.webp",[
    StageGroup(1, [
        t(
            "Dear leader of {nation_name}, please help our climate change marathon's fundraiser.",
            choices={
                "Sure": {"money": -10, "loyalty": +5, "world_opinion" : +10},
                "Nope": {"loyalty": -5, "world_opinion":-5},
            },
        ),
        t(
            "Leader of {nation_name}, our national team needs better training facilities.",
            choices={
                "Approve funding": {"money": -15, "loyalty": +5},
                "Deny funding": {"loyalty": -5},
            },
        ),
        t(
            "Our athletes need new uniforms. Can we get them?",
            choices={
                "Provide new uniforms": {"money": -5, "loyalty": +2},
                "No, use the old ones": {"loyalty": -2},
            },
        ),
        t(
            "Some athletes are requesting personal trainers. Should we approve this?",
            choices={
                "Approve personal trainers": {"money": -8, "loyalty": +3},
                "Deny the request": {"loyalty": -2},
            },
            condition=lambda state: state.money > 50,
        ),
    ]),
    StageGroup(2, [
        t(
            "We've been invited to a major international sports event. Should we participate?",
            choices={
                "Yes, participate": {"money": -20, "world_opinion": +10, "loyalty": +5},
                "No, it's too expensive": {"loyalty": -5, "world_opinion": -5},
            },
        ),
        t(
            "The national team's performance is dropping. Should we invest in a performance coach?",
            choices={
                "Invest in performance coach": {"money": -12, "loyalty": +5, "world_opinion": +3},
                "No, it's unnecessary": {"loyalty": -3, "world_opinion": -2},
            },
            condition=lambda state: state.loyalty < 60,
        ),
        t(
            "One of our top athletes has a serious injury. Should we fund their medical treatment?",
            choices={
                "Yes, fund treatment": {"money": -15, "loyalty": +10},
                "No, it's too costly": {"loyalty": -10},
            },
        ),
    ]),
    StageGroup(3, [
        t("Dear leader of {nation_name}, please help our climate change marathon's fundraiser.",
                 choices = {
                     "Sure": {"money": -45, "loyalty": +5, "world_opinion" : +10},
                     "Nope": {"loyalty": -5, "world_opinion":-5},
                 },
            ),
        t(
            "The marathon was good, but several people were hospitalised due to heatstroke.",
            choices = {"Oh no!": {"money": +30, "world_opinion" : -5}},
            condition = lambda state: state.loyalty>30 and state.money<300,
        ),
        t(
            "The marathon went viral, and we were able to raise a lot of funds.",
            choices = {"Awesome!": {"money": +70, "world_opinion" : +10}},
            condition = lambda state: state.loyalty>50 and state.money<200,
        ),
        t(
            "We have a chance to sign a sponsorship deal with a major brand. Should we proceed?",
            choices={
                "Yes, sign the deal": {"money": +20, "world_opinion": +10},
                "No, it conflicts with our values": {"loyalty": +5, "world_opinion": -5},
            },
            condition=lambda state: state.world_opinion > 50,
        ),
        t(
            "The sports facilities need renovations to meet international standards. Should we invest?",
            choices={
                "Invest in renovations": {"money": -25, "loyalty": +10, "world_opinion": +5},
                "No, they are fine as they are": {"loyalty": -5, "world_opinion": -3},
            },
            condition=lambda state: state.money > 200,
        ),
    ]),
], weight=80)
