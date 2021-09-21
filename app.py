from flask import request
from flask import Flask
from models import Blockchain, Block

app = Flask(__name__)
blockchain = Blockchain()


@app.route('/transactions/new', methods=['POST'])
def create_new_transaction():
    new_transaction = request.get_json()
    blockchain.unconfirmed_transactions.append(new_transaction)
    print('values are :', new_transaction)
    return 'transaction added to unverified pool'


@app.route('/transactions/view', methods=['GET'])
def view_all_transactions():
    chain = blockchain.chain
    ret = ''
    for current in chain:
        ret += str(current.index) + ' '
    print('current unverified transactions are: ')
    print(blockchain.unconfirmed_transactions)
    return ret


@app.route('/transactions/unverified', methods=['GET'])
def view_unverified_transactions():
    return str(blockchain.unconfirmed_transactions)


@app.route('/mine')
def mine_block():
    return 'not mined yet. hang tight :)'


@app.route('/node/register', methods=['POST'])
def register_new_node():
    return 'registered new node'


@app.route('/node/resolve')
def resolve_conflict():
    return 'this is the consensus protocol'


if __name__ == '__main__':
    app.run()
