from flask import request
from flask import Flask, jsonify

from mining import SHA256, hash_calc, hash_calc_block
from models import Blockchain, Block, Transaction, BlockchainEncoder

app = Flask(__name__)
blockchain = Blockchain()
difficulty = 4
reward = 3
home = '127.0.0.1'
passcode = '0000'


@app.route('/transactions/new', methods=['POST'])
def create_new_transaction():
    raw_data = request.get_json()
    new_transaction = Transaction(raw_data['sender'], raw_data['recipient'], raw_data['amount'])
    blockchain.unconfirmed_transactions.append(new_transaction)
    print('values are :', new_transaction)
    return jsonify('New transaction has been added'), 200


@app.route('/transactions/view', methods=['GET'])
def view_all_transactions():
    chain = blockchain.chain
    ret = ''
    for current in chain:
        ret += str(current.index) + ' '
    print('current unverified transactions are: ')
    print(blockchain.unconfirmed_transactions)
    return jsonify(ret)


@app.route('/transactions/unverified', methods=['GET'])
def view_unverified_transactions():
    return str(blockchain.unconfirmed_transactions)


@app.route('/mine', methods=['POST'])
def mine_block():
    # dex needs to check if the given nonce works
    values = request.get_json()
    if len(blockchain.unconfirmed_transactions) == 0:
        return jsonify('no current transactions'), 200
    current_transaction = blockchain.unconfirmed_transactions[0]
    proposed_nonce = values['nonce']
    if values['address'] not in blockchain.registered_nodes:
        return jsonify('you are not authorized to contribute to this network'), 200
    previous_hash = hash_calc_block(blockchain.last_block) # this is skajbfk
    new_hash_mined = hash_calc(len(blockchain.chain), previous_hash, current_transaction, proposed_nonce)
    str_check = '0' * difficulty
    if new_hash_mined.startswith(str_check):
        # create a new block
        new_block = blockchain.new_block(previous_hash=previous_hash, nonce=proposed_nonce)
        reward_transaction = Transaction(sender=home, recipient=values['address'], amount=reward)
        blockchain.unconfirmed_transactions.append(reward_transaction)
        blockchain.chain.append(new_block)
        return jsonify(f'You have been rewarded with {reward}'), 200
    return jsonify('sorry, your nonce did not work :('), 200


@app.route('/node/register', methods=['POST'])
def register_new_node():
    values = request.get_json()
    if values['passcode'] != passcode:
        return jsonify('you are not authorized'), 200
    resp = blockchain.register_node(values['address'])
    return jsonify(resp), 200


@app.route('/chain', methods=['GET'])
def chain():
    return BlockchainEncoder().encode(blockchain), 200


if __name__ == '__main__':
    app.run()
