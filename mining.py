from hashlib import sha256
MAX_NONCE=10000000
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()
def mine(block_number,transactions,previous_hash,prefix_zeros):
    prefix_str='0'*prefix_zeros
    for nonce in range(MAX_NONCE):

        text=str(block_number)+transactions+previous_hash+str(nonce);
        new_hash=SHA256(text);
        if new_hash.startswith(prefix_str):
            print(f"Success Nonce value found to be:{nonce}")
            return new_hash
    raise BaseException(f"couldn't find a Nonce value in the range:{nonce}");


if __name__=='__main__':
    transactions='''
        Dhaval->vhavin->20,
        Mando->cara->45
        '''
    new_hash=mine(5,transactions,'b5d4045c3f466fa91fe2cc6abe79232a1a57cdf104f7a26e716e0a1e2789df78',4)
    print(new_hash)