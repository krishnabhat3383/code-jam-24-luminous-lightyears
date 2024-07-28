"""Craig character template."""

from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t  # noqa: N813

# fmt: off
character = Actor("Craig the Contractor", "url_here",[
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
            choices = {"Take more funds": {"money": -10,  "loyalty" : +10},
                       "Great": {"world_opinion" : +10},
            },
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
            "We have shown great strides in the redevelopment plan, would you hold the inaguration ceremony.",
            choices = {"Yes!": {"money": +5, "loyalty":+10,  "world_opinion" : +10},
                       "No!" : { "loyalty" : -5}},
            condition = lambda state: state.loyalty>40,
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
            "Great! Now the likelihood of floods would be decreased.",
            choices = {"Great!": {"money": +20,  "world_opinion" : +10,  "loyalty" : +10}},
            condition = lambda state: state.loyalty>10,
        ),
    ]),
])
