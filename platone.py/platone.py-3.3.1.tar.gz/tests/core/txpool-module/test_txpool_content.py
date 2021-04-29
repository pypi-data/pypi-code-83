import random

from platone.utils.threads import (
    Timeout,
)


def test_txpool_content(web3_empty):
    web3 = web3_empty

    web3.miner.stop()

    with Timeout(60) as timeout:
        while web3.miner.hashrate or web3.platone.mining:
            timeout.sleep(random.random())

    txn_1_hash = web3.platone.sendTransaction({
        'from': web3.platone.coinbase,
        'to': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
        'value': 12345,
    })
    txn_1 = web3.platone.getTransaction(txn_1_hash)
    txn_2_hash = web3.platone.sendTransaction({
        'from': web3.platone.coinbase,
        'to': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
        'value': 54321,
    })
    txn_2 = web3.platone.getTransaction(txn_2_hash)

    content = web3.txpool.content

    assert web3.platone.coinbase in content['pending']

    pending_txns = content['pending'][web3.platone.coinbase]

    assert txn_1['nonce'] in pending_txns
    assert txn_2['nonce'] in pending_txns

    assert pending_txns[txn_1['nonce']][0]['hash'] == txn_1_hash
    assert pending_txns[txn_1['nonce']][0]['value'] == 12345
    assert pending_txns[txn_2['nonce']][0]['hash'] == txn_2_hash
    assert pending_txns[txn_2['nonce']][0]['value'] == 54321
