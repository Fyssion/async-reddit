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


class RedditException(Exception):
    """Base exception that all exceptions subclass"""
    pass


class ClientException(RedditException):
    """Any excepion that is raised from the :class:`.Client`"""
    pass


class HTTPException(RedditException):
    """Any exception that comes from Reddit
    
    Attributes
    -----------
    response: :class:`aiohttp.ClientResponse`
        The response from Reddit
    """
    def __init__(self, response):
        self.response = response
        self.status = response.status
        super().__init__(f"{response.status}: {response.reason}")


class NotFound(HTTPException):
    """A 404: Not Found exception

    Subclasses :class:`HTTPException`
    """
    pass


class Forbidden(HTTPException):
    """A 403: Forbidden exception

    Subclasses :class:`HTTPException`
    """
    pass


class CannotParseData(ClientException):
    """Raised when the :class:`.Client` cannot parse data from Reddit"""
    pass
