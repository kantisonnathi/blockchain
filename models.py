class Blockchain:
    # list of blocks (let each block have more than one transaction to show ma'am flexibility?)
    def __init__(self, genesis_block):
        self.genesis_block = genesis_block
        self.height = 0
        # figure out the structure or whatever


class Block:
    def __init__(self, prev_hash, transactions, index, ):
        # needs to have a list of transactions
        # needs to have index, date, time and (proof?)
        # also needs to have previous hash.
        # timestamp
        self.transactions = transactions


