from flask import Flask
from web3 import Web3

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
try:
    web3 = Web3(Web3.HTTPProvider(app.config['GANACHE_URL']))
    print('connected to ganache' if web3.isConnected() else 'not connected to ganache')
except Exception as e:
    print(e)

# Path: app\routes\routes.py
from .view import *