# [Defcord](#)

<details open="open">
  <summary>Table Of Contents</summary>
  <ol>
    <li>
      <a href="#about">about</a>
    </li>
    <li>
      <a href="#vital-attributes">Vital Attributes</a>
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

## Gameplay

### `/defcord create`

We use this command to create a defcord game. Whoever creates will be part of the game by default and they'll be the only one who can start the game.

User needs to enter the number of players they want in the game and the nation name they want to be the leader of.

Once the game is created, a message will be posted with the invite code. Other players need to use the invite code to join the game.

A player can join from a different channel or even a different server. Only requirement is in that server `defcord` should be installed.

### `/defcord join`

Other payers need to use this command with the given/taken invite code from the game creator in order to join a `defcord` game.

They also need to enter their nation name.

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
- Include present-time and real information so that the game will give knowledge to players.
- Game time can be configurable by the creator
- Include encryption like mechanism to make it harder for the user
- Option to stop the game by the creator (current work around is to make all players leave)
- Enhance random information picking logic to make it more relevant to the players context and reduce repetitiveness of information
- Option to pause the game

## Contributions
- ...

## Installation
- ...

## Demo

### flow-1
<!-- ![Example](./assets/example.gif) -->


[Move To Top](#defcord)
