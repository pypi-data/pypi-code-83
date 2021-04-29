
def test_miner_setEtherbase(web3_empty):
    web3 = web3_empty
    assert web3.platone.coinbase == web3.platone.accounts[0]
    new_account = web3.personal.newAccount('this-is-a-password')
    web3.miner.setEtherBase(new_account)
    assert web3.platone.coinbase == new_account
