# Auto Econ Agent

Auto Econ Agent is a codebase designed to enable Language Models (LLMs) to interact with the Ethereum blockchain. It provides a set of tools and utilities that make it easy for LLMs to perform various tasks related to Ethereum, such as resolving ENS names, signing transactions, and interacting with Ethereum nodes using JSON-RPC.

## Features

- Resolve ENS names to Ethereum addresses
- Sign Ethereum transactions with a private key
- Interact with Ethereum nodes using JSON-RPC
- Perform calculations using LLMs
- Search the web using SerpAPI
- Make HTTP requests

## Tools

The codebase includes the following tools:

1. **Search**: Uses SerpAPI to search the web and answer questions about current events.
2. **ENS**: Resolves ENS names to valid Ethereum addresses or returns UNRESOLVED if the name is not found.
3. **Requests**: Interacts with HTTP APIs or gets content from webpages.
4. **Sign**: Signs hex-encoded Ethereum transaction objects (keys - 'to', 'value', 'gas', 'gasPrice', 'nonce', 'chainId') with a private key.
5. **Wallet**: Interacts with Ethereum nodes following the JSON-RPC spec. ONLY ACCEPTS JSON PAYLOAD.
6. **Calculator**: Performs calculations using LLMs.

## Setting the Environment

Before running the Auto Econ Agent, you need to set up the environment variables. Create a `.env` file in the project directory and add the following variables:

```
OPENAI_API_KEY=<your_openai_api_key>
SERPAPI_API_KEY=<your_serpapi_api_key>
PRIVATE_KEY=<your_ethereum_private_key>
```

Replace `<your_openai_api_key>`, `<your_serpapi_api_key>`, and `<your_ethereum_private_key>` with your respective API keys and Ethereum private key.

## Usage

To use the Auto Econ Agent, run the `main.py` script using poetry. It will prompt you for input, and you can enter your query or command. The agent will process the input and return the appropriate response.

```python
poetry run app
```

## Code Structure

The codebase is organized into several modules:

1. `main.py`: The main script that initializes the LLM, tools, and agent chain, and handles user input and output.
2. `ens_tool.py`: Contains the `EnsTool` class, which resolves ENS names to Ethereum addresses.
3. `sign.py`: Contains the `Sign` class, which signs Ethereum transactions with a private key.
4. `wallet.py`: Contains the `Wallet` class, which interacts with Ethereum nodes using JSON-RPC.

## Dependencies

The Auto Econ Agent relies on several external libraries:

- `os`: For accessing environment variables
- `dotenv`: For loading environment variables from the `.env` file
- `langchain`: For working with LLMs and providing the base functionality for tools
- `web3`: For interacting with the Ethereum blockchain
- `eth_account`: For signing Ethereum transactions
- `aiohttp`: For making asynchronous HTTP requests
- `async_timeout`: For setting timeouts on asynchronous requests

## Contributing

Contributions to the Auto Econ Agent are welcome. Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Make your changes and commit them to your branch
4. Submit a pull request to the main repository

Please ensure that your code follows the project's coding style and includes appropriate tests and documentation.

## License

The Auto Econ Agent is released under the [MIT License](https://opensource.org/licenses/MIT).
