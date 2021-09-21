import json
from hashlib import sha256
from urllib.parse import urlparse
import time


class Blockchain:
    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    #adding a new node (basically transaction/block) to the list
    #honestly not sure what this is for cuz we have a new_block method
    def register_node(self, address):
        #address of node like http://192.168.0.5:5000
        #netloc contains network location
        parsed_url = urlparse(address)
        if parsed_url.netloc:
            self.unconfirmed_transactions.append(parsed_url.netloc)
        elif parsed_url.path:
            self.unconfirmed_transactions.append(parsed_url.path)
        else:
            raise ValueError('Invalid URL')

    def valid_chain(self, chain):
        #determines if a given blockchain is valid
        #here the parameter chain is the blockchain
        #returns true if valid and false if not
        last_block = chain[0]
        current_index = 1
        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n-------------\n")
            #checking that the hash of the block is right
            last_block_hash = self.hash(last_block)
            if block['previous_hash'] != last_block_hash:
                return False

            #need to check if pow is correct
            #can comment this out if we dont want pow algo
            if not self.valid_proof(last_block['proof'], block['proof'], last_block_hash):
                return False

            last_block = block
            current_index += 1

        return True

    def new_block(self, proof, previous_hash):
        #creating new block in the blockchain

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        #reset current list of transactions (???)
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        #creates transaction to go into next mined block
        #returns index of the block that will hold this transaction

        #TODO: need to keep a condition that adds one transaction per block

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]
    @staticmethod

    def hash(block):
        #creates SHA-256 hash of a block
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()



class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def __repr__(self):
        return 'index: ' + self.index + ', transactions: ' + self.transactions + ', timestamp: ' + self.timestamp

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()




