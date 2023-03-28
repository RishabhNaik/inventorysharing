from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware 
import json


# Connect to the Ethereum network
w3 = Web3(HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

with open('truffle/build/contracts/UserRegistry.json', 'r') as abi_definition:
    info_abi = json.load(abi_definition)

abi = info_abi['abi']  # Paste the ABI of the UserRegistry contract here

# Paste the address of the UserRegistry contract here
contract_address = '0x10892b8ccDdcC7b9aafa61a81677cBc7B66750d5'

# Get the contract instance
contract_instance = w3.eth.contract(address=contract_address, abi=abi)

password = 'hello'
username = 'rishabh'
usertype = 0

# Register the new user


new_account = w3.eth.account.create()
w3.geth.personal.import_raw_key(new_account._private_key.hex(), password)
new_account_address = new_account.address
w3.geth.personal.unlock_account(new_account_address, password)

tx_hash = w3.eth.send_transaction({
    'from': w3.eth.coinbase,
    'to': new_account.address,
    'value': w3.to_wei(10000000000000000, 'ether')
})
w3.eth.wait_for_transaction_receipt(tx_hash)

# tx_hash1 = contract_instance.functions.registerUser(
#     username, int(usertype)).transact({'from': new_account_address})
# w3.eth.wait_for_transaction_receipt(tx_hash1)
# w3.geth.personal.lock_account(new_account_address)


print(f'Accounts on the network: {w3.eth.accounts}')
