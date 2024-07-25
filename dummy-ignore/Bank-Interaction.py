# 2023 Console Cowboys Python Smart Contract Hacking Course
# @author Olie Brown @ficti0n
# http://cclabs.io 

from web3 import Web3

#Make Connection To local Ganache Blockchain
GANACHE = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(GANACHE))
print(f'Connected to Ganache: {web3.is_connected()}')

#Connect to contract
target_address = web3.to_checksum_address("0x87886D504007D41768483E6681bAD2c3d8BE508b")
target_ABI = '[{"inputs":[],"stateMutability":"payable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"},{"indexed":false,"internalType":"string","name":"message","type":"string"}],"name":"DepositLog","type":"event"},{"inputs":[{"internalType":"string","name":"myMessage","type":"string"}],"name":"changeMessage","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"deposit","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"getBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"withdrawAmount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdrawAll","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
target = web3.eth.contract(address=target_address, abi=target_ABI)

first_account = web3.eth.accounts[0]
second_account = web3.eth.accounts[1]
second_account_priv = '0xab1a28876ede9c1f5d85a236206ab7f4bc51d63083635ebd907d534b4167f100'

# print(first_account)

web3.eth.default_account = web3.eth.accounts[1]

print(web3.eth.get_storage_at(target_address, 1).decode())
tx_hash = target.functions.changeMessage('test').transact()
web3.eth.wait_for_transaction_receipt(tx_hash)

print(web3.to_hex(tx_hash))
print(web3.eth.get_transaction(tx_hash))
print(web3.eth.get_storage_at(target_address, 1).decode())

print(target.functions.getBalance().call())

# deposit_eth = target.functions.deposit().buildTransaction({
#     'nonce': web3.eth.getTransactionCount(second_account),
#     'from': second_account,
#     'value': web3.toWei(2, 'ether'),
#     'gas': 3000000,
#     'gasPrice': web3.toWei('20', 'gwei')
# })

# signed_deposit = web3.eth.account.signTransaction(deposit_eth, second_account_priv)
# transaction_hash = web3.eth.sendRawTransaction(signed_deposit.rawTransaction)
# print(web3.toHex(transaction_hash))
# print(web3.eth.get_transaction(transaction_hash))

# print(target.functions.getBalance().call())

# withdraw_eth = target.functions.withdraw(1000000000000000000).buildTransaction({
#                             'nonce': web3.eth.getTransactionCount(web3.eth.accounts[1]),
#                             'from': web3.eth.accounts[1],
#                             'gas': 3000000,
#                             'gasPrice': web3.toWei('50', 'gwei')
#     })

# signed_withdraw = web3.eth.account.signTransaction(withdraw_eth, second_account_priv)
# transaction_hash = web3.eth.sendRawTransaction(signed_withdraw.rawTransaction)
# print(web3.toHex(transaction_hash))
# print(web3.eth.get_transaction(transaction_hash))

# print(target.functions.getBalance().call())