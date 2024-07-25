// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

contract Vulnerable {
    mapping(address => uint256) public balances;

    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        (bool success,) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
        if (balances[msg.sender] > 0) { 
            balances[msg.sender] -= amount; 
        }
    }
}