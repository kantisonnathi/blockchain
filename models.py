import hashlib
import json
from hashlib import sha256
from urllib.parse import urlparse
import time


class Blockchain:
    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()
        self.registered_nodes = ['127.0.0.1']

    def create_genesis_block(self):
        dummy_transaction = Transaction('127.0.0.1', '127.0.0.1', 0)
        genesis_block = Block(0, dummy_transaction, time.time(), "0")
        genesis_block.hash = "genesis block."
        self.chain.append(genesis_block)

    # adding a new node (basically transaction/block) to the list
    # honestly not sure what this is for cuz we have a new_block method
    # K: node is basically a user in the network right
    def register_node(self, address):
        # address of node like http://192.168.0.5:5000
        # netloc contains network location
        """parsed_url = urlparse(address)
        if parsed_url.netloc:
            self.unconfirmed_transactions.append(parsed_url.netloc)
        elif parsed_url.path:
            self.unconfirmed_transactions.append(parsed_url.path)
        else:
            raise ValueError('Invalid URL')
        """
        self.registered_nodes.append(address)

    def valid_chain(self, chain):
        # determines if a given blockchain is valid
        # here the parameter chain is the blockchain
        # returns true if valid and false if not
        last_block = chain[0]
        current_index = 1
        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n-------------\n")
            # checking that the hash of the block is right
            last_block_hash = self.hash(last_block)
            if block['previous_hash'] != last_block_hash:
                return False

            # need to check if pow is correct
            # can comment this out if we dont want pow algo
            if not self.valid_proof(last_block['proof'], block['proof'], last_block_hash):
                return False

            last_block = block
            current_index += 1

        return True

    def new_block(self, previous_hash, nonce):
        # creating new block in the blockchain
        transaction = self.unconfirmed_transactions[0]
        block = Block(index=len(self.chain) + 1, timestamp=time, transaction=transaction, previous_hash=previous_hash,
                      nonce=nonce)
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        """

        self.unconfirmed_transactions.remove(transaction)

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        # creates transaction to go into next mined block
        # returns index of the block that will hold this transaction
        transaction = Transaction(sender, recipient, amount)
        self.unconfirmed_transactions.append(transaction)

        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        # creates SHA-256 hash of a block
        # need to multiply 31 to transaction amount before hashing to ensure #randomness
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def __repr__(self):
        return self.sender + ' ' + self.recipient + ' ' + str(self.amount)


class Block:
    def __init__(self, index, transaction, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transaction = transaction
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def __repr__(self):
        return 'index: ' + self.index + ', transaction: ' + self.transaction + ', timestamp: ' + self.timestamp

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()
