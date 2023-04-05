import os
from dotenv import load_dotenv
from langchain import SerpAPIWrapper, LLMMathChain, OpenAI
from langchain.utilities import RequestsWrapper
from langchain.agents import Tool, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

from .ens_tool import EnsTool
from .wallet import Wallet
from .sign import Sign

load_dotenv()


def get_llm():
    return ChatOpenAI(temperature=0, model_name="gpt-4", openai_api_key=os.environ.get("OPENAI_API_KEY"))


def get_base_llm():
    return OpenAI(temperature=0, model_name="text-davinci-003", openai_api_key=os.environ.get("OPENAI_API_KEY"))


def convert_to_smallest_unit(amount, decimal_places):
    return int(amount * (10 ** decimal_places))


def initialize_tools():
    llm = get_base_llm()

    search = SerpAPIWrapper(search_engine="google",
                            serpapi_api_key=os.environ.get("SERPAPI_API_KEY"))
    ens_chain = EnsTool(
        name="ENS",
        description="Resolves ENS names to valid ethereum addresses or returns UNRESOLVED if the name is not found"
    )

    requests = RequestsWrapper()
    ethereum_rpc = Wallet(
        name="Ethereum RPC", description="Useful for interacting with Ethereum nodes using JSON-RPC")
    llm_math = LLMMathChain(llm=llm)
    sign_tool = Sign(
        name="Sign",
        description="Useful for signing ethereum transaction object with a private key. Transaction parameters must be hex-encoded."
    )

    return [
        Tool(name="Search", func=search.run,
             description="useful for when you need to answer questions about current events"),
        Tool(name="ENS", description="Resolves ENS names to valid ethereum addresses or returns UNRESOLVED if the name is not found", func=ens_chain.run),
        Tool(name="Requests", func=requests.get,
             description="Useful for interacting with HTTP APIs or getting content from webpage"),
        Tool(name="Sign", description="Useful for signing hex-encoded ethereum transaction object(keys - 'to','value', 'gas','gasPrice','nonce','chainId') with a private key.", func=sign_tool.run),
        Tool(name="Wallet",
             description="Useful for interacting with Ethereum nodes following JSON-RPC spec. ONLY ACCEPTS JSON PAYLOAD.",
             func=ethereum_rpc.run),
        Tool(name="Calculator", description="Useful for doing math", func=llm_math.run),
    ]


def main():
    llm = get_llm()
    tools = initialize_tools()
    memory = ConversationBufferMemory(
        memory_key="chat_history", return_messages=True)

    agent_chain = initialize_agent(
        tools,
        llm,
        agent="chat-conversational-react-description",
        verbose=True,
        memory=memory
    )

    input_text = input("How can I help you? ")

    response = agent_chain.run(
        'You are 0xd5028C8CA5223aE981a95da173E2dC362672146B, a helpful, intelligent and resourceful AI wallet. You can create, sign(using Sign) and broadcast transactions(using Wallet).' + input_text)
    print(response)


if __name__ == "__main__":
    main()
