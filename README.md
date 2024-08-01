# [Defcord](#)

<details open="open">
  <summary>Table Of Contents</summary>
  <ol>
    <li>
      <a href="#about">About</a>
    </li>
    <li>
      <a href="#vital-attributes">Vital Attributes</a>
    </li>
    <li>
      <a href="#game-model">Game Model</a>
    </li>
    <li>
      <a href="#commands-available">Commands Available</a>
    </li>
    <li>
      <a href="#theme-relativity">How the bot relate to the theme `Information Overload`</a>
    </li>
    <li>
      <a href="#known-issues">Known Issues</a>
    </li>
    <li>
      <a href="#enchancements">Enchancements</a>
    </li>
    <li>
      <a href="#contributions">Contributions</a>
    </li>
    <li>
      <a href="#installation">Installation of the bot</a>
    </li>
    <li>
      <a href="#Demo">Demo of the game</a>
    </li>
  </ol>
</details>

## About

Defcord is a multiplayer, discord application based game.

You play as a leader of a nation and it is your responsibility to make good decisions based on the information given to you.

You should make sure all of your vital attributes stay positive.

You can't know what vital attributes increase/decrease for the given information for the decision you make because you know, people are complex.

Whoever stays alive till the end of the game is the survivor of the game. If multiple people survive they are also survivors.

The main goal is to make sure you won't run out of your vital attributes in order to survive.

## Vital Attributes

- Money         (default: 100)
- Loyalty       (default: 50)
- Security      (default: 50)
- World Opinion (default: 50)

## Game Model

One player is mapped with only one game. So at a time, a player can game participate in only one game.

The game time will be a random time between `12.5` and `16` minutes.

We have `3` stages, each stage will make the information flow faster.

If the player is AFK or non-responsive to the information for `60` seconds, they're disqualified automatically.

## Commands available


### `/defcord create`

We use this command to create a defcord game. Whoever creates will be part of the game by default and they'll be the only one who can start the game.

User needs to enter the number of players they want in the game and the nation name they want to be the leader of.

Once the game is created, a message will be posted with the invite code. Other players need to use the invite code to join the game.

A player can join from a different channel or even a different server. Only requirement is in that server `defcord` should be installed.


### `/defcord join`

Other payers need to use this command with the given/taken invite code from the game creator in order to join a `defcord` game.

They also need to enter their nation name, via a modal prompt.


### `/defcord start`

Once the required number of players join, the game creator can start the game. Once invoked, the command will automatically start the game that the current player created and part of.

After that, stage `1` begins. Players will receive information at a slow rate first, as the game progresses it'll get faster.

Now the players should start respond to the information by making a good decision in order to survive.


### `/defcord leave`

If the player wants to leave in the middle of the game or before the game start, they can do. But if they leave in the middle of the game, they cannot rejoin. They can join another game.

If you are the last member to quit, you are the survivor of the game as you have no one to compete. But you can play till the game time and see what the game brings you. If you run out of an attribute than you are done.


## Theme Relativity

Given theme is `Information Overload`. Here we try to make the player overwhelmed by giving them information continuously.

They need to keep making good decisions in order to survive. Because they can't give `yes` to all the requests i.e. army tool requests, it'll cost their money. This is also applicable to the reverse situation where the player denies all requests.

After every stage we show the player's attributes so they need to make a quick play to proceed with the next stage. We have AFK mechanism in place so they can't sit idle, information flow till the game end.

## Known Issues

- If you use the `/defcord start` when you didn't create a game or try to start a game again, it'll show as application didn't respond. This is due to a bug where we missed to put an `await` of a response.

## Enhancements

- Include attribute sabotage and request mechanism so that it'll be more PvP instead of PvE.
- Game time can be configurable by the creator.
- Include encryption like mechanism to make it harder for the user.
- Option to stop the game by the creator (current work around is to make all players leave / die).
- Enhance random information picking logic to make it more relevant to the players context and reduce repetitiveness of information.
- Option to pause the game.
- Option to start the game if everyone has not joined.

## Contributions
- Clueless_conoisseur(krishnabhat is Github name) - Checking of some of the PRs and structuring of the project
- Automafun(Dhavantg is Github name) - Basic game character formation, logo making
- Diverman(hazyfossa is Github name) -  Coding of game factory, player classes, Implementation of character templates to the game, Weighted randomness for appreance of characters logic 
- Maheshkumar - Coding of button interactions,  defcord start command, Coding of Advanced UI components
- Sapient - Adding of basic UI elements, coding PlayerState  class' default (instance) values, creating Game class, creating game flow from stages, Adding of Anti AFK, Images for the characters in the game 


## Installation

We require you to have `python 3.12`.

### Clone

```sh
git clone https://github.com/krishnabhat3383/code-jam-24-luminous-lightyears.git
```

if you prefer ssh way,

```sh
git clone git@github.com:krishnabhat3383/code-jam-24-luminous-lightyears.git
```

### Move To Directory

```sh
cd code-jam-24-luminous-lightyears
```

### Create Virtual Environment

```sh
python3 -m venv .venv
```

### Activate Virtual Environment

```sh
source .venv/bin/activate
```

### Install Requirements

```sh
pip install -r requirements.txt
```

### Setup Bot Token

```sh
export DEFCON_BOT_TOKEN=<token>
```

for a persistent way,

```sh
touch .env
```

```sh
echo "DEFCON_BOT_TOKEN=<token>" >> .env
```

### Run The Application

```sh
python main.py
```

## Demo
After the starting of the bot, following would need to be done to start the game. 

1) To initiate the game the player (further referred as 'creator' of the game) need to use `/defcord create` and add the max number of players in the game.
   
   ![Screenshot 2024-08-01 183456](https://github.com/user-attachments/assets/82d6042f-d112-4099-bec1-97625d47e16a)


2) The creator will receive a modal, which will ask for their nation name. 

   ![image](https://github.com/user-attachments/assets/7e306a06-5d21-4a1f-972d-d47db06924e3)


3) After entering the nation name the creator will receive 3 messages.

   ![image](https://github.com/user-attachments/assets/c1e1b135-9d97-44a8-b31b-6e078c04dfeb)

   - 1st message referring to them as a player and their nation name.
   - 2nd message is a game code, for anyone joining the game (visible to everyone in chat)
   - 3rd message is the standard joining message, indicating how many players are left to join and who has last joined (here the game created if of 2 players)


4) Other wannabe players would need to use `/defcord join` with the invite code to join the game

   ![image](https://github.com/user-attachments/assets/045061b9-46f6-45fe-a42c-ca3770548236)


5) After everyone joining the game, everyone in the game will receive this message

   ![image](https://github.com/user-attachments/assets/6d3756e8-6f8e-4c3c-83cc-9d4a8ef1f19d)

    (Here `Thonk` being the last player joined)

6) After this the creator is able to use the command `/defcord start` to start the game, and then everyone will receive 3 messages (3rd one being part of the main game, hence covered below) 

   ![Screenshot 2024-08-01 194118](https://github.com/user-attachments/assets/3da4659d-5671-480b-87ea-da0202571112)
   

   
[Move To Top](#defcord)
