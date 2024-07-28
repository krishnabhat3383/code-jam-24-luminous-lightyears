"""Sandra the spy template information."""

from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t  # noqa: N813

# fmt: off
character = Actor("Sandra the Spy", "https://i.postimg.cc/MKbZzDtj/sandra.webp",[
    StageGroup(1, [
        t(
            "Leader of {nation_name}, we need additional funds to enhance our espionage network.",
            choices={
                "Approve funds": {"money": -15, "security": +5},
                "Deny funds": {"security": -5},
            },
        ),
        t(
            "A rival nation is developing new technology. Should we attempt to steal their plans?",
            choices={
                "Yes, authorize the mission": {"money": -10, "security": +7},
                "No, too risky": {"security": -3},
            },
            condition=lambda state: state.security > 30,
        ),
        t(
            "We have intercepted communications from a potential threat. Should we investigate?",
            choices={
                "Yes, investigate": {"money": -5, "security": +5},
                "No, ignore for now": {"security": -2},
            },
        ),
        t(
            "New security measures in place to protect our nation. Stay vigilant! 🔒 #NationalSecurity #Vigilance",
            choices={
                "Like": {"security": +2},
                "Share": {"security": +3},
                "Ignore": {"loyalty": -1},
            },
            weight=80,
        ),
        t(
            "Top secret mission success! Our spies are the best in the world. 🕵️‍♀️✨ #Espionage #MissionAccomplished",
            choices={
                "Like": {"security": +2},
                "Comment 'Well done!'": {"loyalty": +2},
                "Ignore": {},
            },
            weight=70,
        ),
        t(
            "Daily reminder: Report any suspicious activity to keep our nation safe. 🚨 #SecurityAlert #StaySafe",
            choices={
                "Like": {"security": +1},
                "Share": {"security": +2},
                "Ignore": {},
            },
            weight=120,
        ),
    ]),
    StageGroup(2, [
        t(
            "Our informants have provided intel on an underground organization plotting against us.",
            choices={
                "Act on the intel": {"money": -20, "security": +10},
                "Ignore it": {"security": -5},
            },
            weight=120,
        ),
        t(
            "Spotted: A suspicious activity report that led to a major breakthrough. 📈 #Security #PublicSafety",
            choices={
                "Like": {"security": +2},
                "Share": {"security": +3},
                "Ignore": {},
            },
        ),
        t(
            "A leak has been discovered within our ranks. Should we launch an internal investigation?",
            choices={
                "Yes, investigate": {"money": -10, "security": +5, "loyalty": -3},
                "No, let it be": {"security": -5, "loyalty": +3},
            },
            weight=110,
        ),
        t(
            "Public service announcement: Always stay alert and report anything unusual. 🔔 #Alertness #Security",
            choices={
                "Like": {"security": +1},
                "Share": {"security": +2},
                "Ignore": {},
            },
            weight=130,
        ),
        t(
            "We've identified a mole within our government. Should we apprehend them?",
            choices={
                "Yes, apprehend": {"money": -15, "security": +10},
                "No, watch them": {"security": -3, "loyalty": +2},
            },
            condition=lambda state: state.security > 60,
            weight=130,
        ),
        t(
            "We can sabotage a key project of our rival nation. Should we proceed?",
            choices={
                "Yes, proceed": {"money": -30, "security": +15, "world_opinion": -5},
                "No, hold back": {"security": -5},
            },
            weight=80,
        ),
        t(
            "Our operations have been compromised. Should we relocate our base of operations?",
            choices={
                "Yes, relocate": {"money": -40, "security": +20},
                "No, stay put": {"security": -10},
            },
            weight=80,
        ),
    ]),
    StageGroup(3, [
        t(
            "Our informants have provided intel on an underground organization plotting against us.",
            choices={
                "Act on the intel": {"money": -20, "security": +10},
                "Ignore it": {"security": -5},
            },
        ),
        t(
            "Breaking: We have successfully identified and neutralized a mole. 🕵️‍♀️✅ #Espionage #NationalSecurity",
            choices={
                "Like": {"security": +3},
                "Share": {"security": +4},
                "Ignore": {},
            },
            condition=lambda state: state.security > 60,
        ),
        t(
            "We have a chance to recruit a high-level asset from a rival nation.",
            choices={
                "Recruit the asset": {"money": -25, "security": +15},
                "Pass on the opportunity": {"security": -5},
            },
            condition=lambda state: state.money > 50,
        ),
        t(
            "Here's a spy-themed joke to lighten your day: Why did the spy stay in bed? Because he was undercover! 🤣 #SpyJokes #Humor",  # noqa: E501
            choices={
                "Like": {"loyalty": +1},
                "Share": {"loyalty": +2},
                "Ignore": {},
            },
            weight=120,
        ),
        t(
            "Security tip of the day: How to recognize and report suspicious activities. 🕵️‍♂️🔍 #SecurityTips #PublicSafety",  # noqa: E501
            choices={
                "Like": {"security": +1},
                "Share": {"security": +2},
                "Ignore": {},
            },
            weight=110,
        ),
        t(
            "Our informants have provided intel on an underground organization plotting against us.",
            choices={
                "Act on the intel": {"money": -20, "security": +10},
                "Ignore it": {"security": -5},
            },
        ),
        t(
            "We've identified a mole within our government. Should we apprehend them?",
            choices={
                "Yes, apprehend": {"money": -15, "security": +10},
                "No, watch them": {"security": -3, "loyalty": +2},
            },
            condition=lambda state: state.security > 60,
        ),
        t(
            "We can bribe a key official in a rival nation to gain access to classified information.",
            choices={
                "Yes, bribe them": {"money": -30, "security": +25, "world_opinion": -10},
                "No, too dangerous": {"security": -5},
            },
        ),
        t(
            "A rogue agent has been identified. Should we neutralize them?",
            choices={
                "Yes, neutralize": {"money": -15, "security": +20},
                "No, monitor them": {"security": -5, "loyalty": +3},
            },
        ),
    ]),
], weight=90)
