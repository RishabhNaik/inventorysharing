from web3 import Web3
import json
# HTTPProvider:
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
res = w3.is_connected()
# print(res)

latest_block = w3.eth.get_block('latest')

print(latest_block)

# check_sum = w3.to_checksum_address('0x2924b00c07197FEC47751dB2f293F97e483144a1')
# balance = w3.eth.get_balance(check_sum)
# print(balance)

with open('F:/FYP/inventorysharing/truffle/build/contracts/UserRegistry.json', 'r') as abi_definition:
    info_abi = json.load(abi_definition)

abi=info_abi['abi']


contract_address = '0x5FB21F27464dD9c9960a94637E03c69432b0A3FD'
latest_block_number = w3.eth.block_number

contract_instance = w3.eth.contract(abi=abi, address=contract_address)


account = w3.eth.account.create()
user_address = account.address
user_key = account._private_key.hex()

username=input('Enter your name :')
usertype=int(input('Enter user type'))

function_abi = contract_instance.functions.registerUser(username, usertype).transact({'from': user_address,'gas':6721975})
# print(function_abi)
function_call = w3.eth.account.signTransaction(function_abi, account.privateKey)

# print(user_address+"\n" + user_key)

# Loop through each block and print its information
# for block_number in range(latest_block_number + 1):
#     block = w3.eth.get_block(block_number)
#     print(f"Block #{block['number']}: {block['hash'].hex()}")

# for account in accounts:
#     balance = w3.eth.get_balance(account)
#     print(f"Account: {account}\nBalance: {balance} wei\n")
