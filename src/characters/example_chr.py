from src.templating import Actor, StageGroup
from src.templating import ChoiceTemplate as t

# fmt: off
from models import Actor, StageGroup, Template

# fmt: off
Actor("Fred the Farmer", "url_here",[
    StageGroup(1, [
        Template(
            "Hello, leader of {nation_name}. Can you spare some money for our new farming equipment?",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        Template(
            "Things are great, we managed to grow even more crops than expected.\
                Thank you for your help, leader! \n Here, have this small gift from our community",
            choices = {"Thanks!": {"money": +15}},
            condition = lambda state: state.loyalty>70 and state.money<300,
        ),
    ]),
    StageGroup(2, [
        Template("Hello, leader of {nation_name}. Can you spare some money for our new farming equipment?",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "Things are great, we managed to grow even more crops than expected.\
                Thank you for your help, leader! \n Here, have this small gift from our community",
            choices = {"Thanks!": {"money": +30}},
            condition = lambda state: state.loyalty>90 and state.money<600,
        ),
    ]),
    StageGroup(3, [
        Template("Hello, leader of {nation_name}. Can you spare some money for our new farming equipment?",
                 choices = {
                     "Sure": {"money": -40, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "Things are great, we managed to grow even more crops than expected.\
                Thank you for your help, leader! \n Here, have this small gift from our community",
            choices = {"Thanks!": {"money": +60}},
            condition = lambda state: state.loyalty>110 and state.money<1200,
        ),
    ]),
    StageGroup(4, [
        Template("Hello, leader of {nation_name}. Can you spare some money for our new farming equipment?",
                 choices = {
                     "Sure": {"money": -80, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "Things are great, we managed to grow even more crops than expected.\
                Thank you for your help, leader! \n Here, have this small gift from our community",
            choices = {"Thanks!": {"money": +120}},
            condition = lambda state: state.loyalty>130 and state.money<2400,
        ),
    ]),
    StageGroup(5, [
        Template("Hello, leader of {nation_name}. Can you spare some money for our new farming equipment?",
                 choices = {
                     "Sure": {"money": -160, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "Things are great, we managed to grow even more crops than expected.\
                Thank you for your help, leader! \n Here, have this small gift from our community",
            choices = {"Thanks!": {"money": +240}},
            condition = lambda state: state.loyalty>150 and state.money<480,
        ),
    ]),
])

Actor("Wong the Worker", "url_here",[
    StageGroup(1, [
        Template(
            "O great leader of {nation_name}. May thou be kind enough to raise our minimum wage",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        Template(
            "Thank you! We have been extremely productive and produced so much more goods.",
            choices = {"Great!": {"money": +15}},
            condition = lambda state: state.loyalty>70 and state.money<300,
        ),
    ]),
    StageGroup(2, [
        Template("O great leader of {nation_name}. May thou be kind enough to raise our minimum wage",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "Thank you! We have been extremely productive and produced so much more goods.",
            choices = {"Great!": {"money": +30}},
            condition = lambda state: state.loyalty>90 and state.money<600,
        ),
    ]),
    StageGroup(3, [
        Template("O great leader of {nation_name}. May thou be kind enough to raise our minimum wage",
                 choices = {
                     "Sure": {"money": -40, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "Thank you! We have been extremely productive and produced so much more goods.",
            choices = {"Great!": {"money": +60}},
            condition = lambda state: state.loyalty>110 and state.money<1200,
        ),
    ]),
    StageGroup(4, [
        Template("O great leader of {nation_name}. May thou be kind enough to raise our minimum wage",
                 choices = {
                     "Sure": {"money": -80, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "Thank you! We have been extremely productive and produced so much more goods.",
            choices = {"Great!": {"money": +120}},
            condition = lambda state: state.loyalty>130 and state.money<2400,
        ),
    ]),
    StageGroup(5, [
        Template("O great leader of {nation_name}. May thou be kind enough to raise our minimum wage",
                 choices = {
                     "Sure": {"money": -160, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "Thank you! We have been extremely productive and produced so much more goods.",
            choices = {"Great!": {"money": +240}},
            condition = lambda state: state.loyalty>150 and state.money<480,
        ),
    ]),
])


Actor("Sam the Scientist", "url_here",[
    StageGroup(1, [
        Template(
            "Greetings, esteemed leader of {nation_name}. May I request your consideration for a financial contribution\
                towards our research?",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        Template(
            "Alzhemier's will be cured soon! Thanks for your contribution",
            choices = {"Great!": {"money": +15}},
            condition = lambda state: state.loyalty>70 and state.money<300,
        ),
    ]),
    StageGroup(2, [
        Template("Greetings, esteemed leader of {nation_name}. May I request your consideration for a financial contribution\
                towards our research?",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "Parkinson's will be cured soon! Thanks for your contribution",
            choices = {"Great!": {"money": +30}},
            condition = lambda state: state.loyalty>90 and state.money<600,
        ),
    ]),
    StageGroup(3, [
        Template("Greetings, esteemed leader of {nation_name}. May I request your consideration for a financial contribution\
                towards our research?",
                 choices = {
                     "Sure": {"money": -40, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "AIDS will be cured soon! Thanks for your contribution",
            choices = {"Great!": {"money": +60}},
            condition = lambda state: state.loyalty>110 and state.money<1200,
        ),
    ]),
    StageGroup(4, [
        Template("Greetings, esteemed leader of {nation_name}. May I request your consideration for a financial contribution\
                towards our research?",
                 choices = {
                     "Sure": {"money": -80, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "Hepatitis will be cured soon! Thanks for your contribution",
            choices = {"Great!": {"money": +120}},
            condition = lambda state: state.loyalty>130 and state.money<2400,
        ),
    ]),
    StageGroup(5, [
        Template("Greetings, esteemed leader of {nation_name}. May I request your consideration for a financial contribution\
                towards our research?",
                 choices = {
                     "Sure": {"money": -160, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "CANCER will be cured soon! Thanks for your contribution",
            choices = {"Great!": {"money": +240}},
            condition = lambda state: state.loyalty>150 and state.money<480,
        ),
    ]),
])


Actor("Andy the Athlete", "url_here",[
    StageGroup(1, [
        Template(
            "Dear leader of {nation_name}, please help our climate change marathon's fundraiser.",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        Template(
            "The marathon was phenomenal! Thanks for your support.",
            choices = {"Great!": {"money": +15}},
            condition = lambda state: state.loyalty>70 and state.money<300,
        ),
    ]),
    StageGroup(2, [
        Template("Dear leader of {nation_name}, please help our climate change marathon's fundraiser.",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "The marathon was phenomenal! Thanks for your support.",
            choices = {"Great!": {"money": +30}},
            condition = lambda state: state.loyalty>90 and state.money<600,
        ),
    ]),
    StageGroup(3, [
        Template("Dear leader of {nation_name}, please help our climate change marathon's fundraiser.",
                 choices = {
                     "Sure": {"money": -40, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "The marathon was phenomenal! Thanks for your support.",
            choices = {"Great!": {"money": +60}},
            condition = lambda state: state.loyalty>110 and state.money<1200,
        ),
    ]),
    StageGroup(4, [
        Template("Dear leader of {nation_name}, please help our climate change marathon's fundraiser.",
                 choices = {
                     "Sure": {"money": -80, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "The marathon was phenomenal! Thanks for your support.",
            choices = {"Great!": {"money": +120}},
            condition = lambda state: state.loyalty>130 and state.money<2400,
        ),
    ]),
    StageGroup(5, [
        Template("Dear leader of {nation_name}, please help our climate change marathon's fundraiser.",
                 choices = {
                     "Sure": {"money": -160, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "The marathon was phenomenal! Thanks for your support.",
            choices = {"Great!": {"money": +240}},
            condition = lambda state: state.loyalty>150 and state.money<480,
        ),
    ]),
])


Actor("Aura the Activist", "url_here",[
    StageGroup(1, [
        Template(
            "Kind leader of {nation_name}! Please donate to our LGBTQ+ movement.",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        Template(
            "Rights are Rights! You did the right thing.",
            choices = {"Great!": {"money": +15}},
            condition = lambda state: state.loyalty>70 and state.money<300,
        ),
    ]),
    StageGroup(2, [
        Template("Kind leader of {nation_name}! Please donate to our LGBTQ+ movement.",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "Rights are Rights! You did the right thing.",
            choices = {"Great!": {"money": +30}},
            condition = lambda state: state.loyalty>90 and state.money<600,
        ),
    ]),
    StageGroup(3, [
        Template("Kind leader of {nation_name}! Please donate to our LGBTQ+ movement.",
                 choices = {
                     "Sure": {"money": -40, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "Rights are Rights! You did the right thing.",
            choices = {"Great!": {"money": +60}},
            condition = lambda state: state.loyalty>110 and state.money<1200,
        ),
    ]),
    StageGroup(4, [
        Template("Kind leader of {nation_name}! Please donate to our LGBTQ+ movement.",
                 choices = {
                     "Sure": {"money": -80, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "Rights are Rights! You did the right thing.",
            choices = {"Great!": {"money": +120}},
            condition = lambda state: state.loyalty>130 and state.money<2400,
        ),
    ]),
    StageGroup(5, [
        Template("Kind leader of {nation_name}! Please donate to our LGBTQ+ movement.",
                 choices = {
                     "Sure": {"money": -160, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "Rights are Rights! You did the right thing.",
            choices = {"Great!": {"money": +240}},
            condition = lambda state: state.loyalty>150 and state.money<480,
        ),
    ]),
])


Actor("Sheela the Singer", "url_here",[
    StageGroup(1, [
        Template(
            "Blessed leader of {nation_name}, please fund my public concert!",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        Template(
            "The concert was on fire! Thank you so much.",
            choices = {"Great!": {"money": +15}},
            condition = lambda state: state.loyalty>70 and state.money<300,
        ),
    ]),
    StageGroup(2, [
        Template("Blessed leader of {nation_name}, please fund my public concert!",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "The concert was on firee! Thank you so much.",
            choices = {"Great!": {"money": +30}},
            condition = lambda state: state.loyalty>90 and state.money<600,
        ),
    ]),
    StageGroup(3, [
        Template("Blessed leader of {nation_name}, please fund my public concert!",
                 choices = {
                     "Sure": {"money": -40, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "The concert was on fireee! Thank you so much.",
            choices = {"Great!": {"money": +60}},
            condition = lambda state: state.loyalty>110 and state.money<1200,
        ),
    ]),
    StageGroup(4, [
        Template("Blessed leader of {nation_name}, please fund my public concert!",
                 choices = {
                     "Sure": {"money": -80, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "The concert was on fireeee! Thank you so much.",
            choices = {"Great!": {"money": +120}},
            condition = lambda state: state.loyalty>130 and state.money<2400,
        ),
    ]),
    StageGroup(5, [
        Template("Blessed leader of {nation_name}, please fund my public concert!",
                 choices = {
                     "Sure": {"money": -160, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "The concert was on fireeeee! Thank you so much.",
            choices = {"Great!": {"money": +240}},
            condition = lambda state: state.loyalty>150 and state.money<480,
        ),
    ]),
])


Actor("Craig the Contractor", "url_here",[
    StageGroup(1, [
        Template(
            "Ruler of {nation_name}, the roads need mending following the earthquake.",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        Template(
            "",
            choices = {"Great!": {"money": +15}},
            condition = lambda state: state.loyalty>70 and state.money<300,
        ),
    ]),
    StageGroup(2, [
        Template("Ruler of {nation_name}, the houses need patching following the tornado.",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "Great! Looks like a tornado never hit this place.",
            choices = {"Great!": {"money": +30}},
            condition = lambda state: state.loyalty>90 and state.money<600,
        ),
    ]),
    StageGroup(3, [
        Template("Ruler of {nation_name}, the drains need to be declogged following the flood.",
                 choices = {
                     "Sure": {"money": -40, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "Great! Looks like a flood never hit this place.",
            choices = {"Great!": {"money": +60}},
            condition = lambda state: state.loyalty>110 and state.money<1200,
        ),
    ]),
    StageGroup(4, [
        Template("Ruler of {nation_name}, the electric poles need fixing following the thunderstorm.",
                 choices = {
                     "Sure": {"money": -80, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "Great! Looks like a thunderstorm never hit this place.",
            choices = {"Great!": {"money": +120}},
            condition = lambda state: state.loyalty>130 and state.money<2400,
        ),
    ]),
    StageGroup(5, [
        Template("Ruler of {nation_name}, the city needs to be restored following the tsunami.",
                 choices = {
                     "Sure": {"money": -160, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "Great! Looks like a tsunami never hit this place.",
            choices = {"Great!": {"money": +240}},
            condition = lambda state: state.loyalty>150 and state.money<480,
        ),
    ]),
])


Actor("Gary the General", "url_here",[
    StageGroup(1, [
        Template(
            "Sir, ruler of {nation_name}! The army needs vests Sir!",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        Template(
            "Thanks Sir! Now our army is stronger than ever Sir!",
            choices = {"Great!": {"money": +15}},
            condition = lambda state: state.loyalty>70 and state.money<300,
        ),
    ]),
    StageGroup(2, [
        Template("Sir, ruler of {nation_name}! The army needs equipment Sir!",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "Thanks Sir! Now our army is stronger than ever Sir!",
            choices = {"Great!": {"money": +30}},
            condition = lambda state: state.loyalty>90 and state.money<600,
        ),
    ]),
    StageGroup(3, [
        Template("Sir, ruler of {nation_name}! The army needs weapons Sir!",
                 choices = {
                     "Sure": {"money": -40, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "Thanks Sir! Now our army is stronger than ever Sir!",
            choices = {"Great!": {"money": +60}},
            condition = lambda state: state.loyalty>110 and state.money<1200,
        ),
    ]),
    StageGroup(4, [
        Template("Sir, ruler of {nation_name}! The army needs tanks Sir!",
                 choices = {
                     "Sure": {"money": -80, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "Thanks Sir! Now our army is stronger than ever Sir!",
            choices = {"Great!": {"money": +120}},
            condition = lambda state: state.loyalty>130 and state.money<2400,
        ),
    ]),
    StageGroup(5, [
        Template("Sir, ruler of {nation_name}! The army needs helicopters Sir!",
                 choices = {
                     "Sure": {"money": -160, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "Thanks Sir! Now our army is stronger than ever Sir!",
            choices = {"Great!": {"money": +240}},
            condition = lambda state: state.loyalty>150 and state.money<480,
        ),
    ]),
])


Actor("Sandra the Spy", "url_here",[
    StageGroup(1, [
        Template(
            "ruler of {nation_name}, spy squad needs supplies",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        Template(
            "The supplies helped our mission",
            choices = {"Great!": {"money": +15}},
            condition = lambda state: state.loyalty>70 and state.money<300,
        ),
    ]),
    StageGroup(2, [
        Template("ruler of {nation_name}, spy squad needs supplies",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "The supplies helped our mission",
            choices = {"Great!": {"money": +30}},
            condition = lambda state: state.loyalty>90 and state.money<600,
        ),
    ]),
    StageGroup(3, [
        Template("ruler of {nation_name}, spy squad needs supplies",
                 choices = {
                     "Sure": {"money": -40, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "The supplies helped our mission",
            choices = {"Great!": {"money": +60}},
            condition = lambda state: state.loyalty>110 and state.money<1200,
        ),
    ]),
    StageGroup(4, [
        Template("ruler of {nation_name}, spy squad needs supplies",
                 choices = {
                     "Sure": {"money": -80, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "The supplies helped our mission",
            choices = {"Great!": {"money": +120}},
            condition = lambda state: state.loyalty>130 and state.money<2400,
        ),
    ]),
    StageGroup(5, [
        Template("ruler of {nation_name}, spy squad needs supplies",
                 choices = {
                     "Sure": {"money": -160, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "The supplies helped our mission",
            choices = {"Great!": {"money": +240}},
            condition = lambda state: state.loyalty>150 and state.money<480,
        ),
    ]),
])


Actor("Dave the Doctor", "url_here",[
    StageGroup(1, [
        Template(
            "Great ruler of {nation_name}, we need money to cure those with the flu!",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        Template(
            "",
            choices = {"Great!": {"money": +15}},
            condition = lambda state: state.loyalty>70 and state.money<300,
        ),
    ]),
    StageGroup(2, [
        Template("Great ruler of {nation_name}, we need money to cure those with Alzheimer's!",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "",
            choices = {"Great!": {"money": +30}},
            condition = lambda state: state.loyalty>90 and state.money<600,
        ),
    ]),
    StageGroup(3, [
        Template("Great ruler of {nation_name}, we need money to cure those with Parkinson's!",
                 choices = {
                     "Sure": {"money": -40, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "",
            choices = {"Great!": {"money": +60}},
            condition = lambda state: state.loyalty>110 and state.money<1200,
        ),
    ]),
    StageGroup(4, [
        Template("Great ruler of {nation_name}, we need money to cure those with AIDS!",
                 choices = {
                     "Sure": {"money": -80, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "",
            choices = {"Great!": {"money": +120}},
            condition = lambda state: state.loyalty>130 and state.money<2400,
        ),
    ]),
    StageGroup(5, [
        Template("Great ruler of {nation_name}, we need money to cure those with Hepatitis!",
                 choices = {
                     "Sure": {"money": -160, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "",
            choices = {"Great!": {"money": +240}},
            condition = lambda state: state.loyalty>150 and state.money<480,
        ),
    ]),
])


Actor("Elsa the Engineer", "url_here",[
    StageGroup(1, [
        Template(
            "Ruler of {nation_name}, spare some money to design the army's vests!",
            choices={
                "Sure": {"money": -10, "loyalty": +5},
                "Nope": {"loyalty": -5},
            },
        ),
        Template(
            "The vests are bulletproof! Thanks.",
            choices = {"Great!": {"money": +15}},
            condition = lambda state: state.loyalty>70 and state.money<300,
        ),
    ]),
    StageGroup(2, [
        Template("Ruler of {nation_name}, spare some money to design the army's equipment!",
                 choices = {
                     "Sure": {"money": -20, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "The equipment is top-notch. Thanks.",
            choices = {"Great!": {"money": +30}},
            condition = lambda state: state.loyalty>90 and state.money<600,
        ),
    ]),
    StageGroup(3, [
        Template("Ruler of {nation_name}, spare some money to design the army's weapons!",
                 choices = {
                     "Sure": {"money": -40, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "The weapons are deadly! Thanks.",
            choices = {"Great!": {"money": +60}},
            condition = lambda state: state.loyalty>110 and state.money<1200,
        ),
    ]),
    StageGroup(4, [
        Template("Ruler of {nation_name}, spare some money to design the army's tanks!",
                 choices = {
                     "Sure": {"money": -80, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "The tanks are tanky! Thanks.",
            choices = {"Great!": {"money": +120}},
            condition = lambda state: state.loyalty>130 and state.money<2400,
        ),
    ]),
    StageGroup(5, [
        Template("Ruler of {nation_name}, spare some money to design the army's helicopters!",
                 choices = {
                     "Sure": {"money": -160, "loyalty": +5},
                     "Nope": {"loyalty": -5},
                 },
            ),
        Template(
            "The helicopters are fast! Thanks.",
            choices = {"Great!": {"money": +240}},
            condition = lambda state: state.loyalty>150 and state.money<480,
        ),
    ]),
])


