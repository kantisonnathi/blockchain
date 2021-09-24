### DexCreds

DexCreds is a semi private blockchain made specially for your favourite coffee house - Dexter's coffee!
Anyone can use DexCreds, but only authorized users can mine!

Contact Dexter now :staremoji idk nro:

Different services available:


- /chain - GET - returns json object of the entire blockchain. this includes all the current blocks, unconfirmed transactions, etc.

1) GET http://localhost:5000/chain


2) POST http://localhost:5000/transactions/new
   
    Content-Type: application/json
    Accept: application/json
    {
     "sender": "my address",
     "recipient": "someone else's address",
     "amount": 5
    }

3) POST http://localhost:5000/node/register

    Content-Type: application/json
    {
      "address": "192.31.42.3",
      "passcode": "0000"
    }

4) GET http://localhost:5000/transactions/unverified


5) GET http://localhost:5000/transactions/view

6) POST http://localhost:5000/mine

    Content-Type: application/json
    {
      "address": "192.31.42.3",
      "nonce": 12341
    }

7) GET http://localhost:5000/transaction/current


- /transactions/new - POST method - returns 200 and adds a new transaction to the pool of unconfirmed transactions in the blockchain.
- /node/register - POST - returns 200 and adds the address in the contents to the list of registered nodes for this particular blockchain
- /transactions/unverified - GET - returns a list of all the unverified transactions
- /transactions/view - GET - returns a list of all the blocks in the blockchain (confirmed transactions only)
- /mine - POST - registered users can send in their proposed nonce for the oldest unconfirmed transaction. If the nonce is accepted, the node receives a reward. 


how to send commands using curl - for get and post how 2 do
or send via pycharm
or send via any api tool (like postman)