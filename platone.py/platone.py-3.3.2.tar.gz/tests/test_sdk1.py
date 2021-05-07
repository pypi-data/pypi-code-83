from platone import Web3, HTTPProvider
from platone.platone import Platone
from hexbytes import HexBytes

# get blockNumber
# w3 = Web3(HTTPProvider("http://localhost:6789"))
w3=Web3(HTTPProvider(" http://58.251.94.108:56789"))  #含有国密链的节点
platone = PlatONE(w3)
block_number = platone.blockNumber
print(block_number)

# get Balance
address = 'lax1yjjzvjph3tw4h2quw6mse25y492xy7fzwdtqja'
balance = platone.getBalance(address)
print(balance)

# sendtransaction
to = '0xC1f330B214668beAc2E6418Dd651B09C759a4Bf5'
w3.personal.unlockAccount(address, "password", 60)
data = {
    "from": address,
    "to": to,
    "value": 0x10909,
}
transaction_hex = HexBytes(platone.sendTransaction(data)).hex()
result = platone.waitForTransactionReceipt(transaction_hex)
print(result)