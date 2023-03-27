// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract UserRegistry {
    // Enum to represent the user types
    enum UserType {
        Supplier,
        Retailer
    }

    // Struct to represent a user
    struct User {
        address userAddress;
        string username;
        UserType userType;
    }

    // Dynamic array of all registered users
    User[] public users;

    // Mapping of usernames to user indices
    mapping(string => uint) public usernameToUserIndex;

    // Event that is emitted when a user is registered
    event UserRegistered(
        string username,
        address userAddress,
        UserType userType
    );

    // Function to register a new user
    function registerUser(string memory username, UserType userType) public {
        // Make sure the username is not already taken
        require(
            usernameToUserIndex[username] == 0,
            "Username is already taken"
        );

        // Create a new User struct and add it to the array
        User memory user = User(msg.sender, username, userType);
        users.push(user);
        uint index = users.length;

        // Add the new user's index to the mapping
        usernameToUserIndex[username] = index;

        // Emit the UserRegistered event
        emit UserRegistered(username, msg.sender, userType);
    }

    // Function to get the user associated with a username
    function getUser(string memory username) public view returns (User memory) {
        return users[usernameToUserIndex[username] - 1];
    }
}
