const UserRegistry = artifacts.require("UserRegistry");
const ProductRegistry = artifacts.require("ProductRegistry");

module.exports = async function (deployer) {
  await deployer.deploy(UserRegistry);
  const userRegistryInstance = await UserRegistry.deployed();
  await deployer.deploy(ProductRegistry, userRegistryInstance.address);
};
