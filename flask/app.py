from flask import Flask, render_template, request, redirect, url_for, session
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
import json

app = Flask(__name__)
app.secret_key='xavi3r'
app.debug=True

# Connect to web3 provider
# w3 = Web3(HTTPProvider('https://99cf-157-45-38-25.in.ngrok.io'))
# w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# # Define the contract ABI and address
# with open('truffle/build/contracts/UserRegistry.json', 'r') as abi_definition:
#     info_abi = json.load(abi_definition)

# abi = info_abi['abi']  # Paste the ABI of the UserRegistry contract here

# # Paste the address of the UserRegistry contract here
# contract_address = '0xF52b9E99074b9475dB85762246eA8eBF69E5822a'

# # Get the contract instance
# contract_instance = w3.eth.contract(address=contract_address, abi=abi)



# Define a function to verify the password


# def verify_password(username, password):
#     # Get the Ethereum address associated with the username
#     address = contract_instance.functions.getAddress(username).call()
#     # Unlock the account
#     w3.geth.personal.unlock_account(address, password)
#     # Check if the account is unlocked
#     is_unlocked = w3.geth.personal.list_wallets()[0]['status'] == 'Unlocked'
#     # Lock the account
#     w3.geth.personal.lock_account(address)
#     return is_unlocked

# Define the login and registration routes


# Define the login and registration routes
@app.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == 'POST':
    #     # Get the form data
    #     username = request.form['username']
    #     password = request.form['password']
    #     # Verify the password
    #     if verify_password(username, password):
    #         # Store the username in the session
    #         session['username'] = username
    #         return redirect(url_for('home'))
    #     else:
    #         error = 'Invalid username or password'
    #         return render_template('login.html', error=error)
    # else:
        return render_template('login.html')


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         # Get the form data
#         username = request.form['username']
#         password = request.form['password']
#         user_type = request.form['user_type']
#         # Check if the username is already taken
#         try:
#             existing_user = contract_instance.functions.getUser(username).call()
#             error = 'Username is already taken'
#             return render_template('register.html', error=error)
#         except:
#             pass
#         # Create a new account and import it
#         new_account = w3.eth.account.create()
#         w3.geth.personal.import_raw_key(
#             new_account._private_key.hex(), password)
#         # Unlock the new account
#         w3.geth.personal.unlock_account(new_account.address, password)

#         tx_hash = w3.eth.send_transaction({
#             'from': w3.eth.coinbase,
#             'to': new_account.address,
#             'value': w3.to_wei(10000000000000000, 'ether')
#         })
#         w3.eth.wait_for_transaction_receipt(tx_hash)
#         # Register the new user
#         contract_instance.functions.registerUser(
#             username, int(user_type)).transact({'from': new_account.address})
#         # Lock the account
#         w3.geth.personal.lock_account(new_account.address)
#         # Store the username in the session
#         session['username'] = username
#         return redirect(url_for('home'))
#     else:
#         return render_template('register.html')

# Define the home route


@app.route('/')
def home():
    # Get the username from the session
    # username = session.get('username')
    # if username:
    #     # Get the user type
    #     # user_type = contract_instance.functions.getUserType(username).call()
    #     # return render_template('home.html', username=username, user_type=user_type)
    # else:
    #     return redirect(url_for('login'))
    return render_template('login.html')

# Define the logout route


@app.route('/logout', methods=['GET','POST'])
def logout():
    # Remove the username from the session
    session.clear()
    return redirect(url_for('login'))


@app.route('/s_add_item', methods=['GET', 'POST'])
def s_add_item():
    if request.method == 'POST':
        # Get the form data
        product_name = request.form['product_name']
        product_number = request.form['product_number']
        price = request.form['price']
        quantity = request.form['quantity']
        description = request.form['description']
        # image = request.form['image']
        my_list = [product_name, product_number, price, quantity, description]

        # print(my_list)

        return render_template('s_add_item.html', my_list=my_list)
    else:
        error = 'Invalid data'
        return render_template('s_add_item.html', error=error)


@app.route('/s_item_view')
def s_item_view():

    return render_template("s_item_view.html")

@app.route('/profile')
def profile():

    return render_template("profile.html")


@app.route('/demo')
def demo():

    return render_template("demo.html")

@app.route('/cart')
def cart():

    return render_template("cart.html")


@app.route('/main_inventory')
def main_inventory():

    return render_template("main_inventory.html")


@app.route('/s_inventory')
def s_inventory():

    return render_template("s_inventory.html")


@app.route('/checkout_page')
def checkout_page():

    return render_template("checkout_page.html")

@app.route('/create_session')
def create_session():
    session['name'] = 'Gagz'
    session['username']='Gagz'
    session['usertype']='Supplier'
    session['logged_in']= True

    return redirect(url_for('login'))

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect(url_for('login'))