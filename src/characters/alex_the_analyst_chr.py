"""Alex the analyst media templates and information."""

from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t  # noqa: N813

# fmt: off
character = Actor("Alex the Analyst", "https://i.postimg.cc/D0mxzB3d/Alex.webp",[
    StageGroup(1, [
        t(
            "When the factory gets new machinery and the production line still breaks down. 🤦‍♂️🏭 #FactoryProblems #MondayBlues",  # noqa: E501
            choices={
                "Like": {"loyalty": +1},
                "Share": {"loyalty": +2},
                "Ignore": {},
            },
        ),
        t(
            "Employee of the month: The coffee machine. ☕️🏆 #UnsungHero #OfficeLife",
            choices={
                "Like": {"loyalty": +1},
                "Share": {"loyalty": +2},
                "Ignore": {},
            },
        ),
        t(
            "Joke: Why don't scientists trust atoms? Because they make up everything! 😂🔬 #ScienceJokes #Humor",
            choices={
                "Like": {"loyalty": +1},
                "Share": {"loyalty": +2},
                "Ignore": {},
            },
        ),
        t(
            "Criticism: Our new safety equipment rollout has been slower than anticipated. Workers are concerned. 🛡️🕒 #SafetyFirst #WorkplaceIssues",  # noqa: E501
            choices={
                "Acknowledge": {"loyalty": +2, "security": +2},
                "Ignore": {"loyalty": -1, "security": -1},
            },
        ),
    ]),
    StageGroup(2, [
        t(
            "Meme: When you finally finish a huge project and your boss says, 'Great, now here's another one.' 😅📈 #WorkLife #NeverEndingStory",  # noqa: E501
            choices={
                "Like": {"loyalty": +1},
                "Share": {"loyalty": +2},
                "Ignore": {},
            },
        ),
        t(
            "Criticism: There's been talk about inadequate training programs. Employees feel unprepared. 📚🛠️ #TrainingIssues #WorkplaceConcerns",  # noqa: E501
            choices={
                "Address": {"loyalty": +2},
                "Ignore": {"loyalty": -2},
            },
        ),
        t(
            "Joke: I told my boss three companies were after me and I needed a raise. We laughed. Then I said, 'Seriously, I am going to Amazon, Google, or Netflix if you don not give me a raise.' 😂💼 #JobHumor #SalaryTalks",  # noqa: E501
            choices={
                "Like": {"loyalty": +1},
                "Share": {"loyalty": +2},
                "Ignore": {},
            },
        ),
        t(
            "Positive Feedback: Great job team on hitting our production goals! 🎉📊 #TeamWork #Success",
            choices={
                "Like": {"loyalty": +2},
                "Share": {"loyalty": +3},
                "Ignore": {},
            },
        ),
        t(
            "Meme: When the coffee machine is broken and you have a full day of meetings ahead. ☕️💀 #OfficeStruggles #NeedCoffee",  # noqa: E501
            choices={
                "Like": {"loyalty": +1},
                "Share": {"loyalty": +2},
                "Ignore": {},
            },
        ),
    ]),
    StageGroup(3, [
        t(
            "Meme: When you realize the 'urgent' email you sent an hour ago still has not been read. 📧😩 #EmailProblems #WorkFrustrations",  # noqa: E501
            choices={
                "Like": {"loyalty": +1},
                "Share": {"loyalty": +2},
                "Ignore": {},
            },
        ),
        t(
            "Criticism: Recent changes in work hours are causing stress among workers. Something needs to be done. ⏰😟 #WorkHours #EmployeeWellbeing",  # noqa: E501
            choices={
                "Address": {"loyalty": +3, "security": +2},
                "Ignore": {"loyalty": -3, "security": -2},
            },
        ),
        t(
            "Joke: Why did the scarecrow get a promotion? Because he was outstanding in his field! 😂🌾 #WorkJokes #Promotion",  # noqa: E501
            choices={
                "Like": {"loyalty": +1},
                "Share": {"loyalty": +2},
                "Ignore": {},
            },
        ),
        t(
            "Meme: When you realize it is Friday and you have made it through another week. 🎉🙌 #TGIF #WeekendVibes",
            choices={
                "Like": {"loyalty": +1},
                "Share": {"loyalty": +2},
                "Ignore": {},
            },
        ),
    ]),
], weight=200,
)
