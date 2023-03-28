from flask import Flask

from flask import Flask, render_template, request, session, redirect, url_for
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
import json
# import app

app = Flask(__name__)
app.debug = True

#
# Connect to the Ethereum network
web3 = Web3(HTTPProvider('http://localhost:8545'))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Load the smart contract ABI and address
with open('truffle/build/contracts/UserRegistry.json', 'r') as abi_definition:
    info_abi = json.load(abi_definition)

abi = info_abi['abi']


contract_address = '0x5FB21F27464dD9c9960a94637E03c69432b0A3FD'

# Create an instance of the contract
contract_instance = web3.eth.contract(abi=abi, address=contract_address)

# Function to get the Ethereum address associated with a username


def get_address(username):
    return contract_instance.functions.getAddress(username).call()

# Login route


@app.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == 'POST':
    # Get the form data
    # username = request.form['username']
    # password = request.form['password']

    # Get the Ethereum address associated with the username
    #user_address = get_address(username)

    # Check that the Ethereum address matches the password
    # if user_address and web3.personal.ecRecover(password, username) == user_address:
    # Save the user's address in the session
    #session['user_address'] = user_address
    # return redirect(url_for('home'))
    # else:
    # Login failed, show an error message
    # error = 'Invalid username or password'
    # return render_template('login.html', error=error)
   # else:
    # Show the login form
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get the form data
        username = request.form['username']
        userType = request.form['usertype']

        print(userType)

        # Generate an Ethereum address for the user using the password and username
        account = web3.eth.account.create()
        user_address = account.address

        # Encode the function call data
        # function_abi = contract_instance.functions.registerUser(username, userType).buildTransaction({'from': user_address})
        function_abi = contract_instance.functions.registerUser(
            'my_username', 0).transact({'from': user_address})
        function_call = web3.eth.account.signTransaction(
            function_abi, account.privateKey)

        # Send the transaction to the network
        tx_hash = web3.eth.sendRawTransaction(function_call.rawTransaction)
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

        # Login the user and redirect to the home page
        session['user_address'] = user_address
        return redirect(url_for('home'))
    else:
        # Show the registration form
        return render_template('register.html')


# Home page route
@app.route('/')
def home():
    # Make sure the user is logged in
    # if 'user_address' not in session:
    #     return redirect(url_for('login'))

    # # Get the user's Ethereum address from the session
    # user_address = session['user_address']

    # return render_template('home.html', user_address=user_address)
    return render_template('home.html')

# Logout route


@app.route('/logout')
def logout():
    # Clear the user's session data
    # session.pop('user_address', None)

    # Redirect to the login page
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
