import json
import time

from app import web3



class contract_helper:
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
        pair = []
        for i, (account, private_key) in enumerate(zip(accounts, private_keys)):
            pair.append({
                "account": account,
                "private_key": private_key
            })
        return pair

    def get_all_transactions(self):
        block_number = web3.eth.blockNumber
        transactions = []
        for i in range(block_number + 1):
            block = web3.eth.getBlock(i, full_transactions=True)
            for transaction in block['transactions']:
                transaction_dict = {
                    'hash': transaction.hash.hex(),
                    'blockNumber': transaction.blockNumber,
                    'from': transaction['from'],
                    'to': transaction['to'],
                    'value': web3.fromWei(transaction['value'], 'ether'),
                    'gas': web3.toWei(transaction['gasPrice'], 'gwei'),
                }
                block_timestamp = web3.eth.getBlock(transaction.blockNumber).timestamp
                block_timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(block_timestamp))
                transaction_dict['timeStamp'] = block_timestamp
                transactions.append(transaction_dict)

        return transactions
