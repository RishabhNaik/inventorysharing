from web3 import Web3, Account
import json
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))


res = w3.is_connected()
print(res)

account = w3.eth.account.create()
print(account.address)
user_address = account.address

with open('truffle/build/contracts/UserRegistry.json', 'r') as abi_definition:
    info_abi = json.load(abi_definition)

abi = info_abi['abi']


contract_address = '0x5FB21F27464dD9c9960a94637E03c69432b0A3FD'

# Create an instance of the contract
contract_instance = w3.eth.contract(abi=abi, address=contract_address)

# Function to get the Ethereum address associated with a username


def get_address(username):
    return contract_instance.functions.getAddress(username).call()


function_abi = contract_instance.functions.registerUser('rishabh', 0).transact({'from': user_address, 'gas': 7000})

function_call = w3.eth.account.signTransaction(function_abi, account.privateKey)

# Send the transaction to the network
tx_hash = w3.eth.sendRawTransaction(function_call.rawTransaction)

tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
