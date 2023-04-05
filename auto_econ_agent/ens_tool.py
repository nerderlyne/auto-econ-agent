from langchain.tools import BaseTool
from web3 import HTTPProvider
from ens import ENS

provider = HTTPProvider("https://rpc.ankr.com/eth")
ns = ENS(provider)


class EnsTool(BaseTool):
    def resolve_ens_name(self, query: str):
        try:
            address = ns.address(query)
            if address:
                return address
            else:
                return 'UNRESOLVED'
        except Exception:
            return 'UNRESOLVED'

    def _run(self, query: str) -> str:
        return self.resolve_ens_name(query)

    def _arun(self) -> str:
        return NotImplemented("Not Supported")
