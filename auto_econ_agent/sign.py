from web3 import Web3
import os
from dotenv import load_dotenv
import json
from langchain.tools import BaseTool
from eth_account import Account

load_dotenv()
pk = os.environ.get("PRIVATE_KEY")

class Sign(BaseTool):
    name = "Sign"
    description = "Useful for signing ethereum transaction object with a private key."

    def parse_input(self, transaction: str) -> dict:
        # Check if the transaction input is a JSON string, and if so, convert it to a dictionary
        if isinstance(transaction, str):
            transaction_dict = json.loads(transaction)
        else:
            transaction_dict = transaction

        # Check if the transaction dictionary has the required keys
        required_keys = ["to", "value", "gas", "gasPrice", "nonce", "chainId"]
        for key in required_keys:
            if key not in transaction_dict:
                raise ValueError(
                    f"Missing {key} key in transaction dictionary")
        
       
        for key in ["value", "gas", "gasPrice", "nonce", "chainId"]:
            if isinstance(transaction_dict[key], str):
                if transaction_dict[key].startswith("0x"):
                    transaction_dict[key] = int(
                        transaction_dict[key], 16)
                else:
                    transaction_dict[key] = int(transaction_dict[key])    



        return transaction_dict

    def _run(self, transaction: str) -> dict:
        # Check if the transaction input is a JSON string, and if so, convert it to a dictionary
        transaction_dict = self.parse_input(transaction)
        # Sign the transaction using the private key
        signed_transaction = Account.sign_transaction(transaction_dict, pk)
        return signed_transaction

    def _arun(self) -> dict:
        # Not Supported
        return NotImplemented("Not Supported")
