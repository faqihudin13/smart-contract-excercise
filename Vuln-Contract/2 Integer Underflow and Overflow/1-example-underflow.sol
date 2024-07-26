// SPDX-License-Identifier: unlicensed
pragma solidity ^0.6.0;

contract SafeToken {
    mapping(address => uint256) public balances;
    
    constructor() public {
        balances[msg.sender] = 1000; // Initial supply
    }
    
    function transfer(address to, uint256 amount) public returns (bool) {
        //require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
        balances[to] += amount;
        
        return true; // Indicate success of the function call
    }
    
    function burn(uint256 amount) public returns (bool) {
        //require(balances[msg.sender] >= amount, "Insufficient balance to burn");
        balances[msg.sender] -= amount;
        
        return true; // Indicate success of the function call
    }
}
