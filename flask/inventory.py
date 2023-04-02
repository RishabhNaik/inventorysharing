import json
 # Define the contract ABI and address
with open('truffle/build/contracts/productRegistry.json', 'r') as f:
    info_abi = json.load(f)
    
 


user_abi = info_abi['abi']

# deployment = user_abi['networks']['14333'] 
# user_contract_address = deployment['address']

with open('truffle/build/contracts/productRegistry.json') as f:
    deployment = json.load(f)['networks']['14333']  # Replace 5777 with your network ID
    user_contract_address = deployment['address']

print(user_contract_address)
