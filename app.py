from flask import Flask

app = Flask(__name__)


@app.route('/transactions/new', methods=['POST'])
def create_new_transaction():
    return 'creating new transaction'


@app.route('transactions/view', methods=['GET'])
def view_all_transactions():
    return 'this method is supposed to return a list of all the transactions'


if __name__ == '__main__':
    app.run()
