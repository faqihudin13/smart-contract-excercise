# 2023 Console Cowboys Python Smart Contract Hacking Course
# @author Olie Brown @ficti0n
# http://cclabs.io

from web3 import Web3

#Make Connection To Local Blockchain
GANACHE = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(GANACHE))
print(web3.is_connected())

#Accounts for transactions
first_account = "0x5Ad8c71cE55dd7a967A64EB10271fF2b95Fa30f3"
first_account_private_key = "0x2b2c7414c57cdba13419b5e717b9b086576ae8cd0bf4d590d39d7a0189901694"
second_account = "0xbA4e3fEB6309269539414b3C3A6109Afd941f5C6"

#Build Transaction object
transaction = {
    'nonce': web3.eth.get_transaction_count(first_account),
    'to': second_account,
    'value': web3.to_wei(1, 'ether'),
    'gas': 3000000,
    'gasPrice': web3.to_wei('50', 'gwei')
}

#Sign and Send
signed_transaction = web3.eth.account.sign_transaction(transaction, first_account_private_key)
transaction_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)
print(web3.to_hex(transaction_hash))
print(web3.eth.get_transaction(transaction_hash))