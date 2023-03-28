from web3 import Web3

from web3.middleware import geth_poa_middleware
import json

# Replace with your own endpoint
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

latest_block = w3.eth.get_block('latest')
# print(latest_block)


# Define the contract ABI and address
with open('truffle/build/contracts/UserRegistry.json', 'r') as abi_definition:
    info_abi = json.load(abi_definition)

abi = info_abi['abi']  # Paste the ABI of the UserRegistry contract here

# Paste the address of the UserRegistry contract here
contract_address = '0x10892b8ccDdcC7b9aafa61a81677cBc7B66750d5'

# Get the contract instance
contract_instance = w3.eth.contract(address=contract_address, abi=abi)

print(contract_instance.functions)

username = 'rishabh'
password = 'rishabh'
user_type = 0

# print(contract_instance.functions.usernameToUserIndex(username).call())
# # Check if the username is already taken
# if contract_instance.functions.usernameToUserIndex(username).call() > 0:
#     error = 'Username is already taken'
#     print('error')
# else:
    # Create a new account and import it
new_account = w3.eth.account.create()
w3.geth.personal.import_raw_key(new_account._private_key.hex(), password)
# print(w3.geth.personal.import_raw_key(new_account._private_key.hex(), password))
# w3.geth.personal.import_raw_key(new_account._private_key.hex(), '')
# Unlock the new account
w3.geth.personal.unlock_account(new_account.address, password)
# Register the new user
ci=contract_instance.functions.registerUser(username, int(user_type)).transact({'from': new_account.address})
# print(ci)
# Lock the account
# w3.geth.personal.lock_account(new_account.address)
# Store the username in the session
