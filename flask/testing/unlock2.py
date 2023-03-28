from web3 import Web3, Account
from web3.middleware import geth_poa_middleware


# Specify the URL of the node
url = 'http://localhost:8545'

# Create a Web3 object
web3 = Web3(Web3.HTTPProvider(url))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Get the current block number
block_number = web3.eth.block_number

# Print the block number
print(f'Connected to block {block_number}')

# Get the current block number
block_number = web3.eth.block_number

# Print the block number
print(f'Connected to block {block_number}')

# Create a new account
new_account = web3.eth.account.create()

# Print the account address and private key
print(f'Account address: {new_account.address}')
print(f'Private key: {new_account._private_key.hex() }')

# accounts = web3.eth.accounts

# # print the list of accounts
# print(accounts)

# Add the account to the list of accounts on the network
web3.geth.personal.import_raw_key(new_account._private_key.hex(), '')

# Unlock the account for 60 seconds
web3.geth.personal.unlock_account(new_account.address, '', 60)

print(new_account.address)

tx_hash = web3.eth.send_transaction({
    'from': web3.eth.coinbase,
    'to': new_account.address,
    'value': web3.to_wei(10000000000000000, 'ether')
})
web3.eth.wait_for_transaction_receipt(tx_hash)


# Print the list of accounts on the network
print(f'Accounts on the network: {web3.eth.accounts}')
