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

from datetime import datetime

from .endpoints import BASE_URL

class Subreddit:
    def __init__(self, data):
        data = data["data"]
        self.data = data
        self.display_name = data["display_name"]
        self.display_name_prefixed = data["display_name_prefixed"]
        self.title = data["title"]
        self.header_img = data["header_img"]
        self.icon_img = data["icon_img"]
        self.subscribers = data["subscribers"]
        self.public_description = data["public_description"]
        self.over18 = data["over18"]
        self.description = data["description"]
        self.url = BASE_URL + data["url"]
        self.created_at = datetime.utcfromtimestamp(data["created_utc"])

    def __str__(self):
        return self.display_name_prefixed

class Redditor:
    def __init__(self, data):
        data = data["data"]
        self.data = data
        self.is_employee = data["is_employee"]
        self.name = data["name"]
        self.name_prefixed = "u/" + self.name
        self.link_karma = data["link_karma"]
        self.icon_img = data["icon_img"]
        self.comment_karma = data["comment_karma"]
        self.has_verified_email = data["has_verified_email"]
        self.url = BASE_URL + data["url"]
        self.created_at = datetime.utcfromtimestamp(data["created_utc"])
        self.has_verified_email = data["has_verified_email"]
        self.is_gold = data["is_gold"]
        self.is_mod = data["is_mod"]
        self.verified = data["verified"]
        self.id = data["id"]

        self.subreddit = Subreddit(data["subreddit"])

    def __str__(self):
        return self.name_prefixed

