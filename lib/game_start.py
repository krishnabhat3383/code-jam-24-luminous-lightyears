from interactions import(
    Client,
    Intents,
    listen,
    slash_command,
    SlashContext,
    ContextMenuContext,
    Message,
    message_context_menu,
    Button,
    ButtonStyle,
    component_callback,
    ComponentContext,
    )
from interactions.api.events import Component

from dotenv import load_dotenv
import os
# import asyncio

_ = load_dotenv()
bot = Client(intents=Intents.DEFAULT)
# intents are what events we want to receive from discord, `DEFAULT` is usually fine

users_ids: list[int] = [] #Uhh fix this not being a global thing (idk how to)

@listen()  # this decorator tells snek that it needs to listen for the corresponding event, and run this coroutine
async def on_ready():
    """Ready Indicator"""
    # This event is called when the bot is ready to respond to commands
    print("Ready")

@slash_command(name="start_defcord", description="Welcome to the simulation called DEFCORD")
async def my_command_function(ctx: SlashContext):
    """Basic test 1"""
# Here would need to check are there any other instances of the game
    await ctx.send(f"Starting DEFCORD")
    components = Button(
        style=ButtonStyle.GREEN,
        label="Join",
        custom_id="join_game",
    )
    await ctx.send(f"Player {ctx.user.display_name} has started DEFCORD, Click on Join to join this game", components=components)

@component_callback("join_game")
async def my_callback(ctx: ComponentContext):
    user = ctx.user
    if user.id not in users_ids:
        await ctx.send(f"Player {user.display_name} has joined")
        users_ids.append(user.id)
    else:
        await ctx.send(f"You are already part of the game",ephemeral=True)
    # Cue up the player from here

@message_context_menu(name="repeat")
async def repeat(ctx: ContextMenuContext):
    message: Message = ctx.target
    await ctx.send(message.content)

bot.start(os.getenv("BOT_TOKEN"))
bot.load_extension("interactions.ext.jurigged", poll = True)