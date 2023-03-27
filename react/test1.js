const Web3 = require('web3');
const web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:7545'));


// console.log(web3.eth.net.isListening());

web3.eth.net.isListening()
    .then((isConnected) => {
        if (isConnected) {
            console.log('Host is connected');
        } else {
            console.log('Host is not connected');
        }
    })
    .catch((error) => {
        console.error('Error checking connection:', error);
    });
