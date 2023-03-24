from web3 import Web3
from web3.middleware import construct_sign_and_send_raw_middleware
from eth_account import Account
from web3.middleware import geth_poa_middleware



# Connect to the local Ethereum node
web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Add custom middleware to modify block headers for PoA chain
# def custom_middleware(make_request, web3):
#     def middleware(method, params):
#         if method == 'eth_getBlockByNumber':
#             block = make_request(method, params)
#             if block['extraData'] and len(block['extraData']) > 32:
#                 block['extraData'] = '0x' + block['extraData'][:64]
#             return block
#         else:
#             return make_request(method, params)
#     return middleware

# web3.middleware_onion.add(custom_middleware,'some')

# Create a new account
new_account = Account.create()


# Send some Ether to the new account
tx_hash = web3.eth.send_transaction({
    'from': web3.eth.accounts[0],
    'to': new_account.address,
    'value': web3.to_wei(1, 'ether')
})

print(new_account)

# Wait for the transaction to be mined
web3.eth.wait_For_transaction_receipt(tx_hash)

print(f"New account added to blockchain with address: {new_account.address}")
