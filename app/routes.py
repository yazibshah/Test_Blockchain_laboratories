# app/routes.py

from flask import request, jsonify, Blueprint
from app import app
from app.models import User
from xrpl.clients import JsonRpcClient
from xrpl.wallet import Wallet
import jwt
import datetime

xrpl_client = JsonRpcClient("https://s.altnet.rippletest.net:51234")  # XRPL testnet client

api = Blueprint('api', __name__)

@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User(username=data['username'], email=data['email'], password=data['password'])
    user.save()
    return jsonify({'message': 'User registered successfully'}), 201

@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.objects(username=data['username']).first()
    if user and user.password == data['password']:
        token = jwt.encode({'username': user.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401

@api.route('/balance', methods=['GET'])
def get_balance():
    user = User.objects(username=request.user['username']).first()
    return jsonify({'balance': user.balance})

@api.route('/xrpl_send_payment', methods=['POST'])
def xrpl_send_payment():
    data = request.get_json()
    sender_username = request.user['username']
    recipient_username = data['recipient']
    amount_xrp = data['amount']

    sender = User.objects(username=sender_username).first()
    recipient = User.objects(username=recipient_username).first()

    if sender.balance >= amount_xrp:
        sender_wallet = Wallet(sender.xrpl_secret, xrpl_client)
        recipient_wallet = Wallet(recipient.xrpl_secret, xrpl_client)

        payment_tx = sender_wallet.send_xrp(amount_xrp, recipient_wallet.classic_address)
        response = xrpl_client.submit(payment_tx)

        if response.is_successful():
            sender.balance -= amount_xrp
            recipient.balance += amount_xrp
            sender.save()
            recipient.save()
            return jsonify({'message': 'XRP payment sent successfully'}), 201
        else:
            return jsonify({'message': 'XRP payment failed'}), 500
    else:
        return jsonify({'message': 'Insufficient XRP balance'}), 400
