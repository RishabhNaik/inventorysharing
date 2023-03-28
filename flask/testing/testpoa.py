from web3 import Web3
from web3.middleware import geth_poa_middleware
import json

# HTTPProvider:
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

# add the POA middleware to handle the extraData field
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

res = w3.is_connected()
print(res)

# latest_block = w3.eth.get_block('latest')
# # print(latest_block)

# with open('truffle/build/contracts/UserRegistry.json', 'r') as abi_definition:
#     info_abi = json.load(abi_definition)

# abi=info_abi['abi']
# contract_address = '0x5FB21F27464dD9c9960a94637E03c69432b0A3FD'

# contract_instance = w3.eth.contract(abi=abi, address=contract_address)

print(w3.eth.accounts)
new_account = w3.eth.account.create()
print(new_account)

w3.geth.personal.unlock_account(new_account.address, 'password', 0)

# account = w3.eth.account.create()
# user_address = account.address
# user_key = account._private_key.hex()

# username = 'rishu'
# usertype = 1

# function_abi = contract_instance.functions.registerUser(username, usertype).transact({'from': user_address,'gas':6721975})


# # sign the transaction with the account's private key
# signed_txn = w3.eth.account.sign_transaction(function_abi, private_key=account.private_key)

# # send the signed transaction to the network
# tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

# print(f"Transaction hash: {tx_hash.hex()}")
