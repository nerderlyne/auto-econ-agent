from langchain.agents import ZeroShotAgent
from typing import Optional, Tuple


class CustomZeroShotAgent(ZeroShotAgent):
    def _extract_tool_and_input(self, full_output: str) -> Optional[Tuple[str, str]]:
        try:
            return super()._extract_tool_and_input(full_output)
        except ValueError:
            return None
