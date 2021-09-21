from hashlib import sha256

MAX_NONCE = 10000000


def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def hash_calc(block_number, previous_hash, transaction, nonce):
    text = str(block_number) + str(transaction.amount * 31) + str(transaction) + previous_hash + str(nonce)
    return SHA256(text)


def hash_calc_block(block):
    text = str(block.index) + str(block.transaction.amount*31) + str(block.transaction) + block.previous_hash + str(block.nonce)
    return SHA256(text)


def mine(block_number, transaction_minable, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    for nonce in range(MAX_NONCE):

        text = str(block_number) + transaction_minable + previous_hash + str(nonce)
        new_hash_mined = SHA256(text)
        if new_hash_mined.startswith(prefix_str):
            print(f"Success Nonce value found to be:{nonce}")
            return new_hash_mined
    raise BaseException(f"couldn't find a Nonce value in the range:{MAX_NONCE}")


if __name__ == '__main__':
    transactions = '''
        Dhaval->vhavin->20,
        Mando->cara->45
        '''
    new_hash = mine(5, transactions, 'b5d4045c3f466fa91fe2cc6abe79232a1a57cdf104f7a26e716e0a1e2789df78', 4)
    print(new_hash)
