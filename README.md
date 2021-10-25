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
   - This method returns a list of all the blocks in the blockchain - this includes the index, the transaction 
    and the timestamp of each block


2) POST http://localhost:5000/transactions/new
   
        Content-Type: application/json
        Accept: application/json
        {
         "sender": "my address",
         "recipient": "someone else's address",
         "amount": 5
        }
   - This method allows the sender to append a transaction to the pool of unverified transactions 
    in the blockchain.


3) POST http://localhost:5000/node/register

        Content-Type: application/json
        {
          "address": "192.31.42.3",
          "passcode": "0000"
        }
   - Here, a passcode is set by Dexter. In order to become part of the blockchain, one must 
    obtain the passcode from dexter.
   - If the registration is successful, then the node's address is added to the list of allowed transactions and
    this node can contribute to the blockchain.


4) GET http://localhost:5000/transactions/unverified
    - This method returns a list of all the unverified transactions in the blockchain, if any.
    - If there aren't any, a message saying "There are no unconfirmed transactions" is sent.


5) GET http://localhost:5000/transactions/view
    - This method returns a list of all the verified transactions in the blockchain.


6) GET http://localhost:5000/transaction/current
    
    - This method returns the current transaction in json. 


7) POST http://localhost:5000/allot
    
        Content-Type: application/json
        {
            "address": "192.31.42.3"
        }
   - based on the status of the current node, this method can return three different types of responses depending 
    on the which of the three cases the node could fall under:
     1) The first case is when the node has already received a value (wait - time) for this block - the 
    node is prompted so.
        
     2) The second case is when the node is not registered in the blockchain yet. Since this is a 
    permissioned blockchain, nodes need to be registered before they can take part in the POET 
        consensus.
     3) The third case is when the node is allotted a waiting time. The node to complete its 
    respective waiting time first becomes the leader and is allowed to append a block to the blockchain.
   

8) POST http://localhost/node/complete
        
        Content-Type: application/json
        {
            "address": "192.31.42.3"
        }
    - This method allows the node to check whether or not they have completed waiting their
    allotted time.
    - If enough time has elapsed, then the node is appointed as the leader of this block.  


9) POST http://localhost:5000/node/addBlock
   
        Content-Type: application/json
        {
            "address": "192.31.42.3"
        }
   - Here, the leader appends a block to the blockchain. Since we already have the current transaction, we hash it and append it
    to the chain.

     
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
    

