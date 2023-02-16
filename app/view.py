from flask import render_template, request, jsonify
from app import app

from contract.contract_static import contract_static
from contract.contract_utils import contract_utils

contract_utils = contract_utils()


@app.route('/')
def index():
    return render_template('index.html', data='Home')


@app.route('/balance', methods=['GET'])
def balance():
    address = request.get_json()
    data = contract_utils.get_balance(address['address'])
    return jsonify(data)


@app.route('/accounts', methods=['GET'])
def accounts():
    data = contract_utils.get_accounts()
    return jsonify(data)


@app.route('/send', methods=['POST'])
def send():
    req = request.get_json()
    sender_address, sender_private_key, receiver_address, amount = req['sender_address'], req['sender_private_key'], req['receiver_address'], req['amount']
    result = contract_static(sender_private_key, sender_address, receiver_address, amount).send()
    return jsonify(result.hex())


@app.route('/get_all_transactions', methods=['GET'])
def get_all_transactions():
    data = contract_utils.get_all_transactions()
    return jsonify(data)


