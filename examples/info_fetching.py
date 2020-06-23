import asyncio

import reddit

# NOTE: This library intended to be used along with
# another async library (ex: discord.py), not on it's own.
#
# If you want a standalone reddit library, consider PRAW.
#
# This example exists only to give a basic demo
# on how this lib works.

# Create our client instance
client = reddit.Client()

# Fetch r/github
subreddit = asyncio.run(client.fetch_subreddit("github"))

# Fetch u/FyssionCodes
redditor = asyncio.run(client.fetch_redditor("FyssionCodes"))

# Close the client
asyncio.run(client.close())