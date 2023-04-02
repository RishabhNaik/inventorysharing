// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

 enum UserType {
        None,
        Supplier,
        Retailer
    }

contract UserRegistry {
   

    struct User {
        address userAddress;
        UserType userType;
        string username;
    }

    mapping(string => User) private usernameToUser;
    mapping(address => string) private addressToUsername;

    function registerUser(string memory username, UserType userType) public {
        require(bytes(username).length > 0, "Username cannot be empty");
        require(usernameToUser[username].userAddress == address(0), "Username is already taken");
        address userAddress = msg.sender;
        User memory user = User(userAddress, userType, username);
        usernameToUser[username] = user;
        addressToUsername[userAddress] = username;
    }

    function getUserType(string memory username) public view returns (UserType) {
        User memory user = usernameToUser[username];
        require(user.userAddress != address(0), "User does not exist");
        return user.userType;
    }

    function getAddress(string memory username) public view returns (address) {
        User memory user = usernameToUser[username];
        require(user.userAddress != address(0), "User does not exist");
        return user.userAddress;
    }

    function getUsername() public view returns (string memory) {
        address userAddress = msg.sender;
        string memory username = addressToUsername[userAddress];
        require(bytes(username).length > 0, "User does not exist");
        return username;
    }
}
