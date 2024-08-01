<p align="center" id="defcord">
  <img src="https://github.com/user-attachments/assets/97a9a8f3-9749-4a47-91d8-7bafe9071199" alt="Game Logo" width="200" height="200">
</p>

<h1 align="center">Defcord</h1>

<p align="center"><i>Lead Nations. Compete. Outsmart.</i></p>

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
      <a href="#available-commands">Available Commands</a>
    </li>
    <li>
      <a href="#theme-relativity">How the bot relate to the theme `Information Overload`</a>
    </li>
    <li>
      <a href="#known-issues">Known Issues</a>
    </li>
    <li>
      <a href="#enhancements">Enhancements</a>
    </li>
    <li>
      <a href="#contributions">Contributions</a>
    </li>
    <li>
      <a href="#running-the-app">Running the App</a>
    </li>
    <li>
      <a href="#demo">Demo of the game</a>
    </li>
    <li>
      <a href="#video-showcase">A Video of the Gameplay</a>
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

| Attribute     | Default Value |
|---------------|---------------|
| Money         | 100           |
| Loyalty       | 50            |
| Security      | 50            |
| World Opinion | 50            |

## Game Model

One player is mapped with only one game. So at a time, a player can game participate in only one game.

The game time will be a random time between `12.5` and `16` minutes.

We have `3` stages, each stage will make the information flow faster.

If the player is AFK or non-responsive to the information for `60` seconds, they're disqualified automatically.

## Available Commands


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

- `/defcord start` will show as `Application did not respond` in the invalid use case scenarios instead of showing a relevant message to the user. This is due to a fact that we missed to `await` that message call during a code refactor. Invalid use case scenarios,
  * Trying to start the game without being in one
  * When in a game, trying to start it (only creator can)
  * Trying to start a game is already running
  * Trying to start the game before all the players join
- We have an image embedded in each message to represent the actor of the message. But sometimes the service that we used to host the images goes down. So sometimes the images won't appear. If you receive any error due to this in the console or bot crashes due to this, you can set this env variable `WITHOUT_ACTOR_THUMBNAIL` to `True` to disable thumbnail functionality.

## Enhancements

- Include attribute sabotage and request mechanism so that it'll be more PvP instead of PvE.
- Game time can be configurable by the creator.
- Include encryption like mechanism to make it harder for the user.
- Option to stop the game by the creator (current work around is to make all players leave / die).
- Enhance random information picking logic to make it more relevant to the players context and reduce repetitiveness of information.
- Option to pause the game.
- Option to start the game if everyone has not joined.

## Contributions

- **Clueless_conoisseur** (krishnabhat): Checking PRs, structuring the project
- **Automafun** (Dhanvantg): Basic game character formation, logo creation
- **Diverman** (hazyfossa): Coding game factory, player classes, implementing character templates, weighted randomness logic
- **Maheshkumar**: Coding button interactions, defcord start command, advanced UI components
- **Sapient**: Basic UI elements, PlayerState class default values, Game class creation, game flow, Anti-AFK mechanism, character images

## Running The App

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

    <img src="https://github.com/user-attachments/assets/82d6042f-d112-4099-bec1-97625d47e16a" alt="Game" width="400" height="auto">

2) The creator will receive a modal, which will ask for their nation name.

    <img src="https://github.com/user-attachments/assets/7e306a06-5d21-4a1f-972d-d47db06924e3" alt="Game" width="300" height="auto">

3) After entering the nation name the creator will receive 3 messages.

    1st message referring to them as a player and their nation name.

    2nd message is a game code, for anyone joining the game (visible to everyone in chat)

    3rd message is the standard joining message, indicating how many players are left to join and who has last joined (here the game created if of 2 players)

    </br>

    <img src="https://github.com/user-attachments/assets/c1e1b135-9d97-44a8-b31b-6e078c04dfeb" alt="Game" width="300" height="auto">

4) Other wannabe players would need to use `/defcord join` with the invite code to join the game

    <img src="https://github.com/user-attachments/assets/045061b9-46f6-45fe-a42c-ca3770548236" alt="Game" width="300" height="auto">

5) After everyone joining the game, everyone in the game will receive this message

    <img src="https://github.com/user-attachments/assets/6d3756e8-6f8e-4c3c-83cc-9d4a8ef1f19d" alt="Game" width="300" height="auto">

   (Here `Thonk` being the last player joined)

6) After this the creator is able to use the command `/defcord start` to start the game, and then everyone will receive 3 messages (3rd one being part of the main game, hence covered below)

    <img src="https://github.com/user-attachments/assets/3da4659d-5671-480b-87ea-da0202571112" alt="Game" width="300" height="auto">

7) Game flow - example

    ![flow](https://github.com/user-attachments/assets/df7e944a-a361-47c5-862a-34a4b44f0bf0)


## Video Showcase
https://youtube.com/shorts/Aox39yoCAXY


[Move To Top](#defcord)
