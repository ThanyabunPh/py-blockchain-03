import json

from app import web3


class contract_utils:
    def __init__(self):
        self.private_key_path = 'data/private_keys.csv'

    def get_balance(self, address):
        balance = web3.eth.getBalance(address)
        balance_json = {
            'wei': balance,
            'ether': web3.fromWei(balance, 'ether')
        }
        return balance_json

    def get_accounts(self):
        accounts = web3.eth.accounts
        return json.dumps(accounts)

    def pairAddressPrivateK(self):
        accounts = web3.eth.accounts
        with open(self.private_key_path, 'r') as f:
            private_keys = f.read().splitlines()
        pair = {}
        for i, (account, private_key) in enumerate(zip(accounts, private_keys)):
            pair[i] = {account: private_key}
        return pair

    def get_all_transactions(self):
        block_number = web3.eth.blockNumber
        transactions = []
        for i in range(block_number):
            block = web3.eth.getBlock(i, full_transactions=True)
            if len(block.transactions) > 0:
                transactions.extend(block.transactions)
        return str(transactions)
