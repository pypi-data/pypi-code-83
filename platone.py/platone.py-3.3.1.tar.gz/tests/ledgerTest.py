import json
from hexbytes import HexBytes

from platone import Web3, HTTPProvider, platone, txpool, Account, ledger_node
from platone.ledger import Ledger

rpc = 'http://192.168.16.122:7789'
chain_id = 200
hrp = 'lax'
ledger = 'sys'
main_address, main_private_key = 'lax1jt7m9cs9ryqtqpt939yvhxlqfqc3dscdtvgx8k', 'f90fd6808860fe869631d978b0582bb59db6189f7908b578a886d582cb6fccfa'
user_address, user_private_key = 'lax1apg69eyemch5hxsfw4e2kj94e92la7vt2ucuwr', 'a98e6baea6233965a0740e20e626c5500ecf16121547e8255ee5a28a4f08fc57'



w3 = Web3(HTTPProvider(rpc), chain_id=chain_id, multi_ledger=True, encryption_mode='SM')
platone = platone.Platone(w3)
# platone.defaultAccount = main_address
# txpool = txpool.TxPool(w3)
ledger_node = ledger_node.LedgerNode(w3, 'test10')

print(ledger_node.list())

# 基础call
# print(platone.blockNumber('sys'))
# print(platone.getBalance(main_address, ledger='sys'))
# print(platone.getTransactionCount('lax1jt7m9cs9ryqtqpt939yvhxlqfqc3dscdtvgx8k', ledger='sys'))
# print(txpool.content(ledger))
# print(platone.estimateGas({'data': ''}, ledger=ledger))

# nonce = platone.getTransactionCount(main_address, ledger=ledger)
# print(nonce)

# transaction_dict = {
#     "to": user_address,
#     "gasPrice": 1000000000,
#     "gas": 21000,
#     "nonce": nonce,
#     "data": '',
#     "chainId": chain_id,
#     "value": 1110,
# }
#
# platone.sendTransaction(transaction_dict, ledger=ledger)


# 转账交易
# def transfer(from_privatekey, to_address, amount):
#     from_address = Account.privateKeyToAccount(from_privatekey, hrp, mode='SM').address
#     nonce = platone.getTransactionCount(from_address, ledger=ledger)
#     gas_price = platone.gasPrice(ledger)
#     transaction_dict = {
#         "to": to_address,
#         "gasPrice": gas_price,
#         "gas": 21000,
#         "nonce": nonce,
#         "data": '',
#         "chainId": chain_id,
#         "value": amount,
#     }
#     signedTransactionDict = platone.account.signTransaction(
#         transaction_dict, from_privatekey, net_type=w3.net_type, mode='SM'
#     )
#     data = signedTransactionDict.rawTransaction
#     tx_hash = HexBytes(platone.sendRawTransaction(data, ledger)).hex()
#     result = platone.waitForTransactionReceipt(tx_hash, ledger)
#     return result
#
#
# result = transfer(main_private_key, user_address, 1 * 10 ** 18)
# print(result)


# ABI = [{"constant":False,"inputs":[{"internalType":"string","name":"ledgerJson","type":"string"}],"name":"CreateLedger","outputs":[{"internalType":"int32","name":"","type":"int32"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"GetAllLedgers","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"string","name":"ledgerName","type":"string"},{"internalType":"string","name":"nodeID","type":"string"},{"internalType":"string","name":"blsPubKey","type":"string"}],"name":"JoinLedger","outputs":[{"internalType":"int32","name":"","type":"int32"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"internalType":"string","name":"nodeID","type":"string"}],"name":"JoinedLedgers","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"string","name":"ledgerName","type":"string"},{"internalType":"string","name":"nodeID","type":"string"}],"name":"QuitLedger","outputs":[{"internalType":"int32","name":"","type":"int32"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"string","name":"ledgerName","type":"string"}],"name":"TerminateLedger","outputs":[{"internalType":"int32","name":"","type":"int32"}],"payable":False,"stateMutability":"nonpayable","type":"function"}]
# contract = platone.contract(address=w3.ledger_manager_address, abi=ABI, ledger=ledger)
# print(contract)

# 合约call
# res = contract.functions.GetAllLedgers().call()
# print(f'res: {res}')

# 合约交易
# ledger_json = {
#     "LedgerName": "testLedger",
#     "NodeLedgerInfos": [
#         {
#             "PublicKey": "d1b2ca182eca247050e655964850c03b8d6a2bf70c12723ed68b6cab8d45b40abb45b62983d24ea0d213e334763a530d474b1a9089c133774cd1c0d55603d90b",
#             "nodeType": 1
#         }
#     ]
# }
# txn = contract.functions.CreateLedger(json.dumps(ledger_json)).buildTransaction()
# print(f'txn: {txn}')
# signed_txn = platone.account.signTransaction(txn, private_key=main_private_key, mode='SM')
# tx_hash = platone.sendRawTransaction(signed_txn.rawTransaction, ledger).hex()
# print(f'hash: {tx_hash}')
# res = platone.waitForTransactionReceipt(tx_hash, ledger=ledger)
# print(f'res: {res}')


# ledger = Ledger(w3)
# ledger.is_wait_receipt = True
# ledger_json = {
#     "LedgerName": "testLedger",
#     "NodeLedgerInfos": [
#         {
#             "PublicKey": "d1b2ca182eca247050e655964850c03b8d6a2bf70c12723ed68b6cab8d45b40abb45b62983d24ea0d213e334763a530d474b1a9089c133774cd1c0d55603d90b",
#             "nodeType": 1
#         }
#     ]
# }
# result = ledger.createLedger(json.dumps(ledger_json), main_private_key)
# print(result)
