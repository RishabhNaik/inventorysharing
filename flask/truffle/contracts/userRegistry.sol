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
    }

    // Mapping of usernames to users
    mapping(string => User) private users;

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
            users[username].userAddress == address(0),
            "Username is already taken"
        );

        // Create a new User struct and add it to the mapping
        User memory user = User(msg.sender, userType);
        users[username] = user;

        // Emit the UserRegistered event
        emit UserRegistered(username, msg.sender, userType);
    }

    // Function to get the Ethereum address associated with a username
    function getAddress(string memory username) public view returns (address) {
        return users[username].userAddress;
    }

    // Function to get the user type associated with a username
    function getUserType(
        string memory username
    ) public view returns (UserType) {
        return users[username].userType;
    }
}
