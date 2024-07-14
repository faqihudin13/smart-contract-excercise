# 2023 Console Cowboys Python Smart Contract Hacking Course
# @author Olie Brown @ficti0n
# http://cclabs.io

from web3 import Web3

#Make Connection To Local Blockchain
GANACHE = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(GANACHE))
print(web3.is_connected())

#Accounts for transactions
first_account = "0x7A1E86F65f90298641011D121de2E5c95D5FdC94"
first_account_private_key = "0x150132990404f6e66ed5cbbd3b61fd1aa14228ff1e06685bb76777628ce9f9e1"
second_account = "0xFb3E3D3AF7B780cD229C39bc0fC268AAa44De9BF"

#Build Transaction object
transaction = {
    'nonce': web3.eth.getTransactionCount(first_account),
    'to': second_account,
    'value': web3.toWei(1, 'ether'),
    'gas': 3000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

#Sign and Send
signed_transaction = web3.eth.account.signTransaction(transaction, first_account_private_key)
transaction_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)
print(web3.toHex(transaction_hash))
print(web3.eth.get_transaction(transaction_hash))