from flask import request
from flask import Flask, jsonify

from mining import SHA256, hash_calc, hash_calc_block
from models import Blockchain, Block, Transaction, BlockchainEncoder

app = Flask(__name__)
blockchain = Blockchain()  # creating an instance of the Blockchain class definted in app.py
difficulty = 4  # difficulty specifies the number of 0s that should precede the hash
reward = 3  # reward is the number of DexCreds that a node is awarded with if it presents the right nonce
home = '127.0.0.1'  # specifies Dexter's address
passcode = '0000'  # passcode for security purposes - registering a new node

dictionary_poet = {}


@app.route('/transactions/new', methods=['POST'])
def create_new_transaction():
    """
    Data is sent in JSON with 3 key-value pairs:
    sender - the address of the sender
    recipient - the address of the recipient
    amount - the number of DexCreds that are being transferred
    :return: 200 in case of success
    """
    raw_data = request.get_json()
    new_transaction = Transaction(raw_data['sender'], raw_data['recipient'], raw_data['amount'])  # instantiating a transaction object
    blockchain.unconfirmed_transactions.append(new_transaction)  # appending it to the blockchains transaction
    # print('values are :', new_transaction)
    return jsonify('New transaction has been added'), 200


@app.route('/transactions/view', methods=['GET'])
def view_all_transactions():  # this method returns a list of all the confirmed transactions
    ret = ''
    for current in blockchain.chain:
        ret += str(current.transaction) + '\n'
    return ret


@app.route('/transactions/unverified', methods=['GET'])
def view_unverified_transactions():  # this method returns a list of all the unconfirmed transactions
    return str(blockchain.unconfirmed_transactions)


@app.route('/mine', methods=['POST'])
def mine_block():
    # dex needs to check if the given nonce works
    values = request.get_json()
    if len(blockchain.unconfirmed_transactions) == 0:
        # there are no unconfirmed transactions
        return jsonify('no current transactions'), 200

    curr_transaction = blockchain.unconfirmed_transactions[0]  # the transaction for which a block is being mined
    proposed_nonce = values['nonce']
    if values['address'] not in blockchain.registered_nodes:
        return jsonify('You are not authorized to contribute to this network'), 200

    previous_hash = hash_calc_block(blockchain.last_block)
    new_hash_mined = hash_calc(len(blockchain.chain), previous_hash, curr_transaction, proposed_nonce)

    str_check = '0' * difficulty
    if new_hash_mined.startswith(str_check):
        # creating a new block because the nonce is acceptable
        new_block = blockchain.new_block(previous_hash=previous_hash, nonce=proposed_nonce)
        reward_transaction = Transaction(sender=home, recipient=values['address'], amount=reward)
        blockchain.unconfirmed_transactions.append(reward_transaction)
        blockchain.chain.append(new_block)
        return jsonify(f'You have been rewarded with {reward}'), 200
    return jsonify('sorry, your nonce did not work :('), 200


@app.route('/node/register', methods=['POST'])
def register_new_node():  # registering a new node in the network that is authorized to mine blocks
    values = request.get_json()
    if values['passcode'] != passcode:
        return jsonify('you are not authorized'), 200
    resp = blockchain.register_node(values['address'])
    return jsonify(resp), 200


@app.route('/node/allot', methods=['POST'])
def allot_random_time():
    values = request.get_json()
    address = values['address']
    if address in dictionary_poet:
        return jsonify('You have already been allotted a time'), 200


@app.route('/chain', methods=['GET'])
def chain():  # returns a json object of the entire blockchain
    return BlockchainEncoder().encode(blockchain), 200


@app.route('/transaction/current', methods=['GET'])
def current_transaction():  # returns the transaction that needs to be mined
    if len(blockchain.unconfirmed_transactions) == 0:
        return 'There are no transactions to mine at the moment, please try again later'
    transaction = blockchain.unconfirmed_transactions[0]
    return transaction


if __name__ == '__main__':
    app.run()
