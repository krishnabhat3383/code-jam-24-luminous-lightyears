"""National media templates and information."""

from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t  # noqa: N813

# fmt: off
character = Actor("National Media", "https://i.postimg.cc/VsTY8Wpz/defcord.webp", [
    StageGroup(1, [
        t(
            "Trending Now: A rumor is spreading that neighboring nations are stockpiling weapons. Should we respond?",
            choices={
                "Yes, increase military spending": {"money": -20, "security": +5, "world_opinion": -10},
                "No, it's just a rumor": {"security": -5, "world_opinion": +5},
            },
        ),
        t(
            "Viral Post: A celebrity is urging people to boycott local produce due to pesticide use. Should we address this?",  # noqa: E501
            choices={
                "Yes, ban the use of pesticides": {"money": -15, "loyalty": +5, "world_opinion": +5},
                "No, ignore the celebrity": {"loyalty": -5, "world_opinion": -5},
            },
        ),
        t(
            "Breaking News: A popular social media figure claims your administration is hiding a health crisis. Should we respond?",  # noqa: E501
            choices={
                "Yes, launch a PR campaign": {"money": -10, "loyalty": +5, "security": +5},
                "No, it's not true": {"loyalty": -5, "world_opinion": -5},
            },
        ),
    ]),
    StageGroup(2, [
        t(
            "Hashtag Alert: #NoMoreTaxes is trending. Citizens are protesting against the latest tax hike. Should we lower taxes?",  # noqa: E501
            choices={
                "Yes, lower taxes": {"money": -20, "loyalty": +10, "world_opinion": +5},
                "No, maintain the current tax rate": {"loyalty": -5, "world_opinion": -5},
            },
        ),
        t(
            "Misinformation: False reports of a natural disaster in a key agricultural region are causing panic. Should we allocate emergency funds?",  # noqa: E501
            choices={
                "Yes, allocate emergency funds": {"money": -15, "security": +5, "world_opinion": +5},
                "No, verify the reports first": {"security": -5, "world_opinion": -5},
            },
        ),
        t(
            "Influencer Post: A famous influencer is promoting a controversial new technology. Should we adopt this technology?",  # noqa: E501
            choices={
                "Yes, adopt the technology": {"money": -25, "loyalty": +10, "world_opinion": +5},
                "No, it's too risky": {"loyalty": -5, "world_opinion": -5},
            },
        ),
    ]),
    StageGroup(3, [
        t(
            "Trending Conspiracy: A conspiracy theory is circulating that the government is spying on citizens. Should we address this?",  # noqa: E501
            choices={
                "Yes, deny the accusations": {"money": -10, "security": +5, "world_opinion": +5},
                "No, ignore it": {"security": -5, "world_opinion": -5},
            },
        ),
        t(
            "False Alarm: A fake news article claims that a neighboring nation is planning an attack. Should we prepare for war?",  # noqa: E501
            choices={
                "Yes, prepare for war": {"money": -30, "security": +10, "world_opinion": -10},
                "No, investigate the claim first": {"security": -5, "world_opinion": +5},
            },
        ),
        t(
            "Viral Challenge: A dangerous social media challenge is encouraging people to vandalize public property. Should we address this?",  # noqa: E501
            choices={
                "Yes, launch a public awareness campaign": {"money": -15, "loyalty": +5, "world_opinion": +5},
                "No, it's just a phase": {"loyalty": -5, "world_opinion": -5},
            },
        ),
        t(
            "Social Media Pressure: Users are demanding immediate action on climate change. Should we implement drastic measures?",  # noqa: E501
            choices={
                "Yes, implement drastic measures": {"money": -20, "security": +5, "world_opinion": +10},
                "No, take a more measured approach": {"security": -5, "world_opinion": -5},
            },
        ),
    ]),
], weight=200)
