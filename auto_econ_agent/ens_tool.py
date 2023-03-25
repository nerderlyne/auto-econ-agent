import asyncio
from langchain.tools import BaseTool
from web3 import HTTPProvider
from ens import ENS

provider = HTTPProvider("https://rpc.ankr.com/eth")
ns = ENS(provider)


class EnsTool(BaseTool):
    name = "ENS Resolver"
    description = "Resolves an ENS name to its corresponding address"

    async def resolve_ens_name(self, query: str):
        try:
            address = ns.address(query)
            if address:
                return address
            else:
                return 'UNRESOLVED'
        except Exception:
            return 'UNRESOLVED'

    def _run(self, query: str) -> str:
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self._arun(query))

    async def _arun(self, query: str) -> str:
        return await self.resolve_ens_name(query)
