import aiohttp

from interfaces.async_http_reader import AsyncHttpReader


class AiohttpReader(AsyncHttpReader):
    """
    Implementation of asynchronous HTTP reader based on aiohttp library
    """
    def __init__(self):
        self.client = aiohttp.ClientSession(raise_for_status=True)

    async def get_text(self, url: str) -> str:
        async with self.client.get(url=url) as response:
            return await response.text()

    async def close(self):
        await self.client.close()
