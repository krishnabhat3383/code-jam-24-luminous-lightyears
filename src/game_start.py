from interactions import (
    ActionRow,
    Button,
    ButtonStyle,
    ComponentContext,
    Embed,
    Extension,
    Modal,
    ModalContext,
    ShortText,
    SlashContext,
    component_callback,
    modal_callback,
    slash_command,
)

users_ids: list[int] = []  # Global Var for the players in the game


class GameInitiation(Extension):
    """Control the extension entry point."""

    @slash_command(name="start_defcord", description="Welcome to the simulation called DEFCORD")
    async def my_command_function(self, ctx: SlashContext) -> None:
        """Start the game of DEFCORD."""
        # Here would need to check are there any other instances of the game
        components = ActionRow(
            Button(
                style=ButtonStyle.GREEN,
                label="Join",
                custom_id="join_game",
            ),
            Button(
                style=ButtonStyle.RED,
                label="Leave",
                custom_id="leave_game",
            ),
        )
        embed = Embed(
            title="Starting DEFCORD",
            description=f"The tactical game of DEFCORD has been initiated by <@{ctx.user.id}>",
            color=(255, 0, 0),
        )
        await ctx.send(embed=embed, components=components)

    @component_callback("join_game")
    async def join_callback(self, ctx: ComponentContext) -> None:
        """Control player joining the game."""
        # Need to make this channel wise
        user = ctx.user
        if user.id not in users_ids:
            nation_modal = Modal(
                ShortText(label="Type the name of your nation", custom_id="nation_name"),
                title="Select Name of the nation",
                custom_id="Nation_name",
            )
            await ctx.send_modal(modal=nation_modal)
        else:
            await ctx.send("You are already part of the game", ephemeral=True)

    @component_callback("leave_game")
    async def leave_callback(self, ctx: ComponentContext) -> None:
        """Control players leaving the game."""
        user = ctx.user
        if user.id in users_ids:
            await ctx.send(f"Player <@{user.id}> has left")
            users_ids.remove(user.id)
        else:
            await ctx.send("You are not part of the game", ephemeral=True)

    @modal_callback("Nation_name")
    async def nation_name (self, ctx: ModalContext, nation_name: str) -> None:
        """Send Nation name to player and program."""
        await ctx.send(f"You have joined as the nation of {nation_name}", ephemeral=True)
        users_ids.append(ctx.user.id)
        if nation_name:
            await ctx.send(f"Player <@{ctx.user.id}> has joined")
        # here we can extract the nation name
