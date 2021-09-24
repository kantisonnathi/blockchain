### DexCreds

DexCreds is a semi private blockchain made specially for your favourite coffee house - Dexter's coffee!
Anyone can use DexCreds, but only authorized users can mine!

Contact Dexter now :staremoji idk nro:

Different services available:


- /chain - GET - returns json object of the entire blockchain. this includes all the current blocks, unconfirmed transactions, etc.

1) GET http://localhost:5000/chain



- /transactions/new - POST method - returns 200 and adds a new transaction to the pool of unconfirmed transactions in the blockchain.
- /node/register - POST - returns 200 and adds the address in the contents to the list of registered nodes for this particular blockchain
- /transactions/unverified - GET - returns a list of all the unverified transactions
- /transactions/view - GET - returns a list of all the blocks in the blockchain (confirmed transactions only)
- /mine - POST - registered users can send in their proposed nonce for the oldest unconfirmed transaction. If the nonce is accepted, the node receives a reward. 

more:

// apis 