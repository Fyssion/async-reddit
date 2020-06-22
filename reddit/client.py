"""
MIT License

Copyright (c) 2020 Fyssion

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import asyncio

import aiohttp
from async_timeout import timeout

from .objects import Subreddit, Redditor
from .errors import NotFound, Forbidden, HTTPExeption, InvalidData
from .endpoints import SUBREDDIT_URL, REDDITOR_URL, JSON_URL


class Client:
    def __init__(self, *, loop=None, session=None):
        self.log_in = None
        self.loop = loop or asyncio.get_event_loop()
        self.session = session or aiohttp.ClientSession(loop=self.loop)

    async def get_headers(self):
        if not self.log_in:
            return {}
        else:
            raise NotImplementedError

    async def _fetch(self, url):
        try:
            async with timeout(30.0):
                headers = await self.get_headers()

                async with self.session.get(url, headers=headers) as resp:

                    if resp.status != 200:
                        if resp.status == 404:
                            raise NotFound(resp)
                        elif resp.status == 403:
                            raise Forbidden(resp)
                        else:
                            raise HTTPExeption(resp)

                    data = await resp.json()

        # If the request times out, raise a better error
        except asyncio.TimeoutError:
            raise asyncio.TimeoutError(f"Timed out while fetching '{url}'")

        return data

    async def fetch_subreddit(self, name):
        url = SUBREDDIT_URL + name + JSON_URL

        data = await self._fetch(url)

        # Subreddit kind is t5
        if data["kind"] != "t5":
            raise InvalidData("Data kind does not match request.")

        try:
            subreddit = Subreddit(data)
        except KeyError:
            raise InvalidData("Could not parse subreddit data from Reddit.")

        return subreddit

    async def fetch_redditor(self, name):
        url = REDDITOR_URL + name + JSON_URL

        data = await self._fetch(url)

        # Redditor kind is t2
        if data["kind"] != "t2":
            raise InvalidData("Data kind does not match request.")

        try:
            redditor = Redditor(data)
        except KeyError:
            raise InvalidData("Could not parse redditor data from Reddit.")

        return redditor
