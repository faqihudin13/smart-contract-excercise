// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EtherStore {
    mapping(address => uint) public balances;

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint _amount) public {
        uint bal = balances[msg.sender];
        require(bal >= _amount, "Insufficient balance");

        (bool sent, ) = msg.sender.call{value: _amount}("");
        require(sent, "Failed to send Ether");

        balances[msg.sender] -= _amount;
    }

    // Helper function to check the balance of this contract
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}
pragma solidity 0.8.13;

// SPDX-License-Identifier: UNLICENSED

contract ChainWallet {
    mapping(address => uint256) private balances;

    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw() external {
        uint256 balance = getUserBalance(msg.sender);

        // Checks user's balance.
        require(balance > 0, "Insufficient balance");

        // Sends all the user's balance to them.
        (bool success, ) = msg.sender.call{value: balance}(""); // At this point, the caller's code is executed.
        require(success, "Failed to send Ether");

        // Updates the user's balance after sending them their entire balance.
        balances[msg.sender] = 0;
    }

    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }

    function getUserBalance(address _user) public view returns (uint256) {
        return balances[_user];
    }
}