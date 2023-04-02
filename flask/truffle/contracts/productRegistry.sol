// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./userRegistry.sol";

contract ProductRegistry {
    struct Product {
        string name;
        uint256 price;
        string description;
        uint256 quantity;
    }

    mapping(uint256 => Product) private products;
    UserRegistry private userRegistry;

    constructor(address _userRegistry) {
        userRegistry = UserRegistry(_userRegistry);
    }

    function addProduct(uint256 _id, string memory _name, uint256 _price, string memory _description, uint256 _quantity) public {
        require(userRegistry.getUserType(userRegistry.getUsername()) == UserType.Supplier, "Only suppliers can add products");
        require(products[_id].price == 0, "Product ID already exists");
        products[_id] = Product(_name, _price, _description, _quantity);
    }

    function editProduct(uint256 _id, string memory _name, uint256 _price, string memory _description, uint256 _quantity) public {
        require(userRegistry.getUserType(userRegistry.getUsername()) == UserType.Supplier, "Only suppliers can edit products");
        require(products[_id].price != 0, "Product does not exist");
        products[_id] = Product(_name, _price, _description, _quantity);
    }

    function viewProduct(uint256 _id) public view returns (string memory, uint256, string memory, uint256) {
        require(products[_id].price != 0, "Product does not exist");
        Product memory product = products[_id];
        return (product.name, product.price, product.description, product.quantity);
    }

    function deleteProduct(uint256 _id) public {
        require(userRegistry.getUserType(userRegistry.getUsername()) == UserType.Supplier, "Only suppliers can delete products");
        require(products[_id].price != 0, "Product does not exist");
        delete products[_id];
    }

    function viewAllProducts() public view returns (Product[] memory) {
        uint256 count = 0;
        for (uint256 i = 1; i <= 1000; i++) {
            if (products[i].price != 0) {
                count++;
            }
        }
        Product[] memory allProducts = new Product[](count);
        uint256 index = 0;
        for (uint256 i = 1; i <= 1000; i++) {
            if (products[i].price != 0) {
                allProducts[index] = products[i];
                index++;
            }
        }
        return allProducts;
    }
}
