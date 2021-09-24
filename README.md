### DexCreds

<h1>Dexter's Coffee House!</h1>

DexCreds is a semi private blockchain made specially for your favourite coffee house - Dexter's coffee!
Anyone can use DexCreds, but only authorized users can mine!

Welcome to Dexter's coffee shop! 

Step 1: Order a coffee!!
If you want to order a coffee, call request (2). This method returns 200 and adds a new transaction to the pool 
of unconfirmed transactions in the blockchain.

Step 2: Wait for the magic!
Dexter and his employees will brew a delicious coffee for you, and in the meanwhile, your transaction will be verified and appended to the blockchain.

Step 3: Enjoy your drink!
If you have enough computational resources, feel free to mine and earn 3 DexCreds per successful mine!

Different services available:

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

How to send GET & POST requests?
1. Using cURL:
    1. GET command:
        curl https://localhost:5000/transaction/current
       
    2. POST command:
        curl -d '{json}' -H 'Content-Type: application/json' https://localhost:5000/mine
        where 'json' can be replaced with the data that needs to be sent
       
Note: The above 2 commands are prototypes, please check the listings above (services available) to send the required requests.

2. Via PyCharm

3. Via any API tool available (such as postman)
    
    

------------------------------------------------------------------------------------------------------------
- /chain - GET - returns json object of the entire blockchain. this includes all the current blocks, unconfirmed transactions, etc.
- /node/register - POST - returns 200 and adds the address in the contents to the list of registered nodes for this particular blockchain
- /transactions/unverified - GET - returns a list of all the unverified transactions
- /transactions/view - GET - returns a list of all the blocks in the blockchain (confirmed transactions only)
- /mine - POST - registered users can send in their proposed nonce for the oldest unconfirmed transaction. If the nonce is accepted, the node receives a reward. 
