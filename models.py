import hashlib
import json
from hashlib import sha256
import time
from mining import hash_calc_block

from flask.json import JSONEncoder


class Blockchain:
    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()
        self.registered_nodes = ['127.0.0.1']  # the home address is registered by default
        self.leader_nodes = []

    def create_genesis_block(self):
        dummy_transaction = Transaction('127.0.0.1', '127.0.0.1', 0)
        # a dummy transaction of 0 is added in the genesis block
        genesis_block = Block(0, dummy_transaction, time.time(), "0")
        genesis_block.hash = "genesis block."
        self.chain.append(genesis_block)

    def register_node(self, address):
        if address in self.registered_nodes:
            return 'Already registered'
        self.registered_nodes.append(address)
        return 'Registered new Node'

    def new_block(self, previous_hash, nonce):
        # creating new block in the blockchain
        transaction = self.unconfirmed_transactions[0]
        block = Block(index=len(self.chain) + 1, timestamp=time.time(), transaction=transaction, previous_hash=previous_hash,
                      nonce=nonce)

        self.unconfirmed_transactions.remove(transaction)
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        # creates transaction to go into next mined block
        # returns index of the block that will hold this transaction
        transaction = Transaction(sender, recipient, amount)
        self.unconfirmed_transactions.append(transaction)
        return self.last_block['index'] + 1

    def valid_chain(self):
        idx = len(self.chain)
        for i in range(0, len(self.chain) - 1):
            fblock = self.chain[i]
            sblock = self.chain[i + 1]
            if hash_calc_block(fblock) != sblock.previous_hash:
                idx = i + 1  # the block at index i+1 is invalid
                break

        if idx == len(self.chain):  # this means no blocks are invalid -> the blockchain is valid
            return

        # blocks after idx are removed
        for i in range(0, len(self.chain)):
            if i >= idx:
                self.chain.remove(self.chain[i])
                i -= 1

    @property
    def last_block(self):
        return self.chain[-1]


class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def __repr__(self):
        return 'sender: ' + str(self.sender) + ', recipient: ' + str(self.recipient) + ', amount: ' + str(self.amount)


class Block:
    def __init__(self, index, transaction, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transaction = transaction
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def __repr__(self):
        print(self.timestamp)
        return 'index: ' + str(self.index) + ', transaction: ' + str(self.transaction) + ', timestamp: ' \
               + str(self.timestamp)


class BlockchainEncoder(JSONEncoder):  # this block enables us to convert the blockchain to json format
    def default(self, o):
        return o.__dict__
