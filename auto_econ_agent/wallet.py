import json
import aiohttp
import asyncio
from async_timeout import timeout
from langchain.tools import BaseTool


class Wallet(BaseTool):
    name = "Wallet"
    description = "Useful for sending JSON-RPC requests to Ethereum nodes"

    def _run(self, payload: str) -> str:
        """Use the tool."""
        loop = asyncio.get_event_loop()

        # Ensure the coroutine is wrapped in a future and run until complete
        result = asyncio.ensure_future(self._arun(payload))
        return loop.run_until_complete(result)

    async def _arun(self, payload: str) -> str:
        """Use the tool asynchronously."""
        json_payload = json.loads(payload)
        async with aiohttp.ClientSession() as session:
            async with timeout(10):  # Set a timeout for the request
                async with session.post("https://rpc.ankr.com/eth", json=json_payload) as response:
                    return await response.text()
