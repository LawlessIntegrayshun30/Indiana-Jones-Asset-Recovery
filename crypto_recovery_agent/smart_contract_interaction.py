## smart_contract_interaction.py
from web3 import Web3
from typing import Any, List

class SmartContractInteraction:
    def __init__(self, web3_url: str = "http://127.0.0.1:8545"):
        self.web3 = Web3(Web3.HTTPProvider(web3_url))
        self.contract = None

    def connect_to_contract(self, address: str, abi: List[Any]) -> None:
        """
        Connect to an Ethereum smart contract using its address and ABI.
        
        :param address: The Ethereum address of the smart contract.
        :param abi: The ABI of the smart contract.
        """
        if not self.web3.isConnected():
            raise ConnectionError("Unable to connect to the Ethereum node.")
        if not self.web3.isAddress(address):
            raise ValueError(f"The address {address} is not a valid Ethereum address.")
        self.contract = self.web3.eth.contract(address=self.web3.toChecksumAddress(address), abi=abi)

    def execute_contract_function(self, function_name: str, params: List[Any], from_address: str = None) -> Any:
        """
        Execute a function of the connected smart contract.
        
        :param function_name: The name of the function to execute.
        :param params: The parameters to pass to the function.
        :param from_address: The Ethereum address from which the transaction is made.
        :return: The result of the function execution.
        """
        if self.contract is None:
            raise RuntimeError("Smart contract is not connected. Call connect_to_contract() first.")
        contract_function = self.contract.get_function_by_name(function_name)(*params)
        if from_address:
            return contract_function.transact({'from': from_address})
        else:
            return contract_function.call()
