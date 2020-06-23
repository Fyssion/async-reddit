# This example assumes you have discord.py installed

from discord.ext import commands
import discord

import traceback
import reddit


class ExampleBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")

        self.reddit = reddit.Client()

    async def on_ready(self):
        print(f"Logged in as {self.user.name} - {self.user.id}")

    async def close(self):
        await super().close()
        await self.reddit.close()


bot = ExampleBot()


@bot.command()
async def subreddit(ctx, *, name):
    subreddit = await bot.reddit.fetch_subreddit(name)

    # Basic information display, you can add to this
    em = discord.Embed(
        title=subreddit.title,
        description=subreddit.public_description,
        url=subreddit.url,
        color=discord.Color.red(),
    )

    em.add_field(name="Subscribers:", value=subreddit.subscribers)

    if subreddit.icon_img:
        em.set_thumbnail(url=subreddit.icon_img)

    await ctx.send(embed=em)


@bot.command()
async def redditor(ctx, *, name):
    redditor = await bot.reddit.fetch_redditor(name)

    em = discord.Embed(
        title=redditor.name,
        description=redditor.description,
        url=redditor.url,
        color=discord.Color.red(),
    )

    karma = user.comment_karma + user.link_karma
    em.add_field(name="Karma:", value=str(karma))

    args = redditor.icon_img.split("?")
    icon = args[0]
    em.set_thumbnail(url=icon)

    await ctx.send(embed=em)


@subreddit.error
@redditor.error
async def handle_reddit_errors(ctx, error):
    traceback.print_exception(type(error), error, error.__traceback__)
    if isinstance(error, commands.CommandInvokeError):
        original = error.original

        if isinstance(original, reddit.NotFound):
            query = discord.utils.escape_markdown(ctx.args[-1])
            await ctx.send(f"I couldn't find `{query}`. Sorry.")

        elif isinstance(original, reddit.Forbidden):
            await ctx.send("Sorry, I couldn't access that from Reddit.")


bot.run("token_here")
