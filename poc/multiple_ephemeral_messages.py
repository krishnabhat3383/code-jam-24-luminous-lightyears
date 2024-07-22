import asyncio

from interactions import (
    Button,
    ButtonStyle,
    ChannelType,
    Client,
    GuildText,
    Intents,
    Modal,
    ModalContext,
    OptionType,
    ParagraphText,
    ShortText,
    SlashContext,
    listen,
    slash_command,
    slash_option,
)
from interactions.api.events import Component

bot = Client(intents=Intents.DEFAULT)


@listen()
async def on_ready() -> None:  # noqa: D103
    print("Ready")
    print(f"This bot is owned by {bot.owner}")


@slash_command(name="my_command")
@slash_option(
    name="channel_option",
    description="Channel Option",
    required=True,
    opt_type=OptionType.CHANNEL,
    channel_types=[ChannelType.GUILD_TEXT],
)
async def my_command_function(ctx: SlashContext, channel_option: GuildText) -> None:  # noqa: D103
    await channel_option.send("This is a text channel in a guild")
    for i in range(1, 10):
        await ctx.send("Message#" + str(i), ephemeral=True)


@slash_command(name="my_modal")
async def my_modal_function(ctx: SlashContext) -> None:  # noqa: D103
    my_modal = Modal(
        ShortText(label="Short Input Text", custom_id="short_text"),
        ParagraphText(label="Long Input Text", custom_id="long_text"),
        title="My Modal",
        custom_id="my_modal",
    )
    await ctx.send_modal(modal=my_modal)
    modal_ctx: ModalContext = await ctx.bot.wait_for_modal(my_modal)

    short_text = modal_ctx.responses["short_text"]
    long_text = modal_ctx.responses["long_text"]

    await modal_ctx.send(
        f"Short text: {short_text}, Paragraph text: {long_text}",
        ephemeral=True,
    )

    for i in range(1, 10):
        asyncio.sleep(1)
        await ctx.send("Message#" + str(i), ephemeral=True)


@slash_command(name="give_me_lot_of_messages")
async def my_modal_unction(ctx: SlashContext) -> None:  # noqa: D103
    async def check(component: Component) -> bool:
        if component.ctx.author.username.startswith("a"):
            return True
        else:  # noqa: RET505
            await component.ctx.send(
                "Your name does not starts with 'a'",
                ephemeral=True,
            )
            for i in range(1, 3):
                await asyncio.sleep(1)
                await component.ctx.send("Message#" + str(i), ephemeral=True)
            return True

    button_1 = Button(
        custom_id="my_button_id",
        style=ButtonStyle.GREEN,
        label="Click Me",
    )

    button_2 = Button(
        custom_id="my_button_id",
        style=ButtonStyle.GREEN,
        label="Click Me",
    )

    button_3 = Button(
        custom_id="my_button_id",
        style=ButtonStyle.GREEN,
        label="Click Me",
    )

    await ctx.send(
        "Look a Button!",
        components=button_1,
        ephemeral=True,
    )

    for i in range(1, 3):
        await asyncio.sleep(1)
        await ctx.send("Message#" + str(i), ephemeral=True)

    await ctx.send(
        "Look a Button!",
        components=button_2,
        ephemeral=True,
    )

    for i in range(1, 3):
        await asyncio.sleep(1)
        await ctx.send("Message#" + str(i), ephemeral=True)

    await ctx.send(
        "Look a Button!",
        components=button_3,
        ephemeral=True,
    )

    try:
        await bot.wait_for_component(
            components=[button_1],
            check=check,
            timeout=10,
        )
        await bot.wait_for_component(
            components=[button_2],
            check=check,
            timeout=10,
        )
        await bot.wait_for_component(
            components=[button_3],
            check=check,
            timeout=10,
        )
    except Exception as e:  # noqa: BLE001
        print(e)


bot.start("")
