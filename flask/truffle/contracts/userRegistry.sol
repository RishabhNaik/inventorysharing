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
        UserType userType;
        string username;
    }

    // Array of all registered users
    User[] private users;

    // Function to get the index of the user in the users array given a username
    function usernameToUserIndex(string memory username) public view returns (uint) {
        for (uint i = 0; i < users.length; i++) {
            if (keccak256(bytes(users[i].username)) == keccak256(bytes(username))) {
                return i;
            }
        }
        return uint(-1);
    }

    // Event that is emitted when a user is registered
    event UserRegistered(
        string username,
        address userAddress,
        UserType userType
    );

    // Function to register a new user
function usernameToUserIndex(string memory username) public view returns (uint) {
    for (uint i = 0; i < users.length; i++) {
        if (keccak256(bytes(users[i].username)) == keccak256(bytes(username))) {
            return i;
        }
    }
    return type(uint256).max;
}

        // Create a new User struct and add it to the array
        User memory user = User(msg.sender, userType, username);
        uint userIndex = users.length;
        users.push(user);

        // Emit the UserRegistered event
        emit UserRegistered(username, msg.sender, userType);
    }

    // Function to get the Ethereum address associated with a username
function getAddress(string memory username) public view returns (address) {
    uint index = usernameToUserIndex(username);
    require(index != type(uint256).max, "User does not exist");
    return users[index].userAddress;
}

    // Function to get the user type associated with a username
 function getUserType(string memory username) public view returns (UserType) {
    uint index = usernameToUserIndex(username);
    require(index != type(uint256).max, "User does not exist");
    return users[index].userType;
}

    // Function to update a user's information
    function updateUser(
        string memory username,
        UserType userType
    ) public {
        uint index = usernameToUserIndex(username);
        require(index != uint(-1), "User does not exist");
        require(users[index].userAddress == msg.sender, "Only the user can update their information");
        users[index].userType = userType;
    }
}
