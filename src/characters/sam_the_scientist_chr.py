"""Scientist template information."""

from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t  # noqa: N813

# fmt: off
character = Actor("Sam the Scientist", "https://i.postimg.cc/xTSTr7G2/sam.webp",[
    StageGroup(1, [
        t(
            "Greetings, esteemed leader of {nation_name}. May I request your consideration for a financial contribution towards our research?",  # noqa: E501
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        t(
            "Exciting news! Our team has just published a paper on renewable energy solutions. 🌱📄 #GreenEnergy #ScientificResearch",  # noqa: E501
            choices={
                "Like": {"world_opinion": +2},
                "Share": {"world_opinion": +3},
                "Ignore": {"loyalty": -5},
            },
        ),
        t(
            "Hello, {nation_name}! Our research team needs funding to continue our groundbreaking work on renewable energy.",  # noqa: E501
            choices={
                "Approve funding": {"money": -20, "world_opinion": +5, "security": +3},
                "Deny funding": {"loyalty": -5},
            },
        ),
        t(
            "We've developed a new technique to increase crop yields. Should we implement it?",
            choices={
                "Yes, implement it": {"money": -10, "world_opinion": +3, "loyalty": +5},
                "No, not now": {"loyalty": -3},
            },
            condition=lambda state: state.money > 50,
        ),
        t(
            "We've been invited to collaborate on a climate change project with international scientists.",
            choices={
                "Join the project": {"money": -15, "world_opinion": +7},
                "Decline": {"loyalty": -2},
            },
            weight=110,
        ),
        t(
            "Here's a fun fact: Did you know that our new crop yield technique could increase food production by 30%? 🍅 #Agriculture #FoodSecurity",  # noqa: E501
            choices={
                "Like": {"loyalty": +2},
                "Comment 'Amazing!'": {"loyalty": +3},
                "Ignore": {"loyalty": -1},
            },
            condition=lambda state: state.loyalty > 30,
            weight=150,
        ),
    ]),
    StageGroup(2, [
        t(
            "Our lab needs new equipment to stay competitive in biotech research.",
            choices={
                "Buy the equipment": {"money": -30, "security": +5, "loyalty": +3},
                "Delay the purchase": {"loyalty": -4},
            },
        ),
        t(
            "We've been invited to present our findings at an international conference.",
            choices={
                "Attend the conference": {"money": -25, "world_opinion": +10},
                "Decline the invitation": {"world_opinion": -5},
            },
            condition=lambda state: state.world_opinion > 40,
        ),
        t(
            "A major corporation wants to fund our research in exchange for some control over our findings.",
            choices={
                "Accept the funding": {"money": +40, "loyalty": -5, "world_opinion": -3},
                "Reject the funding": {"loyalty": +5, "world_opinion": +3},
            },
        ),
    ]),
    StageGroup(3, [
        t(
            "We've discovered a potential cure for a common disease. Should we proceed with human trials?",
            choices={
                "Approve the trials": {"money": -40, "world_opinion": +15, "security": +10},
                "Delay the trials": {"loyalty": -5},
            },
            condition=lambda state: state.security > 60,
        ),
        t(
            "A foreign government has offered to fund our research in exchange for shared knowledge.",
            choices={
                "Accept the offer": {"money": +50, "world_opinion": +5, "security": -10},
                "Decline the offer": {"world_opinion": -3},
            },
        ),
        t(
            "We've made a breakthrough in AI technology that could revolutionize various industries.",
            choices={
                "Invest in AI": {"money": -50, "world_opinion": +20, "security": +10},
                "Hold off for now": {"loyalty": -7},
            },
        ),
        t(
            "Today's science joke: Why did the biologist look forward to casual Fridays? Because they're allowed to wear genes! 🤣 #ScienceJokes #FunFact",  # noqa: E501
            choices={
                "Like": {"loyalty": +1},
                "Share": {"loyalty": +2},
                "Ignore": {"loyalty": -5},
            },
            weight=200,
        ),
        t(
            "We've entered a new international collaboration. Excited for the future of science! 🌏 #GlobalResearch #ScienceTogether",  # noqa: E501
            choices={
                "Retweet": {"world_opinion": +5},
                "Comment 'Fantastic!'": {"loyalty": +3},
                "Ignore": {"world_opinion": -5},
            },
            weight=150,
        ),
        t(
            "Science trivia: What's the most abundant gas in Earth's atmosphere? Nitrogen! 🧠🌍 #ScienceFacts #Trivia",
            choices={
                "Like": {"loyalty": +1},
                "Share": {"world_opinion": +2},
                "Ignore": {"loyalty": -1},
            },
            weight=150,
        ),
    ]),
], weight=120)
