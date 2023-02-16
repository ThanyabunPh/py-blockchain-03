from app import web3


class contract_static:
    def __init__(self, private_key, sender_address, receiver_address, amount):
        self.private_key = private_key
        self.sender_address = sender_address
        self.receiver_address = receiver_address
        self.amount = amount

    def create_transaction(self):
        transaction = {
            'to': self.receiver_address,
            'value': web3.toWei(self.amount, 'ether'),
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': web3.eth.getTransactionCount(self.sender_address)
        }
        return transaction


    def sign_transaction(self, transaction):
        signed_tx = web3.eth.account.signTransaction(transaction, self.private_key)
        return signed_tx


    def send_transaction(self, signed_tx):
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return tx_hash

    def send(self):
        transaction = self.create_transaction()
        signed_tx = self.sign_transaction(transaction)
        tx_hash = self.send_transaction(signed_tx)
        return tx_hash

