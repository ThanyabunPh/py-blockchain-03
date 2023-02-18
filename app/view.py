from flask import render_template, request, jsonify
from app import app

from contract.contract_static import contract_static
from contract.contract_helper import contract_helper

contract_utils = contract_helper()


@app.route('/')
def index():
    accounts_pair = contract_utils.pairAddressPrivateK()
    transactions = contract_utils.get_all_transactions()
    return render_template('index.html', accounts_pair=accounts_pair, transactions=transactions)


@app.route('/balance', methods=['POST'])
def balance():
    address = request.get_json()
    data = contract_utils.get_balance(address['address'])
    balance_data = {
        'wei': data['wei'],
        'ether': data['ether']
    }
    return jsonify(balance_data)


@app.route('/accounts', methods=['GET'])
def accounts():
    data = contract_utils.get_accounts()
    return jsonify(data)


@app.route('/send', methods=['POST'])
def send():
    req = request.get_json()
    sender_private_key = req['sender_private_key']
    sender_address = req['sender_address']
    receiver_address = req['receiver_address']
    amount = req['amount']
    result = contract_static(sender_private_key, sender_address, receiver_address, amount).send()
    return result


@app.route('/get_all_transactions', methods=['GET'])
def get_all_transactions():
    data = contract_utils.get_all_transactions()
    return jsonify(data)


