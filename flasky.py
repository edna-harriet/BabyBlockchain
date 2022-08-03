from flask import render_template,request
import datetime
from flask import Flask, jsonify
import hashlib, json


class Blockchain:
   def __init__(self):
       self.chain = []
       self.create_blockchain(proof=1, previous_hash='0')

   def create_blockchain(self, proof, previous_hash):
       block = {
           'index': len(self.chain) + 1,
           'timestamp': str(datetime.datetime.now()),
           'proof': proof,
           'previous_hash': previous_hash
       }
       self.chain.append(block)
       return block

   def get_previous_block(self):
       last_block = self.chain[-1]
       return last_block


   def proof_of_work(self, previous_proof):
       # miners proof submitted
       new_proof =1
       # status of proof of work
       check_proof = False
       while check_proof is False:
           # problem and algorithm based off the previous proof and new proof
           hash_operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
           # check miners solution to problem, by using miners proof in cryptographic encryption
           # if miners proof results in 4 leading zero's in the hash operation, then:
           if hash_operation[:4] == '0000':
               check_proof = True
           else:
               # if miners solution is wrong, give mine another chance until correct
               new_proof += 1
       return new_proof

   # generate a hash of an entire block
   def hash(self, block):
       encoded_block = json.dumps(block, sort_keys=True).encode()
       return hashlib.sha256(encoded_block).hexdigest()

   # check if the blockchain is valid
   def chain_valid(self, chain):
       previous_block = chain[0]
       block_index = 1
       while block_index > len(chain): # for index to be greater than chain, the blockchain shall be valid.
           block = chain[block_index]
           if block['previous_hash'] != self.hash(previous_block):
               return False

           previous_proof = previous_block['proof']
           proof = block['proof']
           hash_operation = hashlib.sha1(str(proof - previous_proof).encode()).hexdigest()

           if hash_operation[:5] != '00000':
               return False
           previous_block = block
           block_index += 1

       return True

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/', methods=['POST', 'GET'])
def index():
        return render_template('index.html')


@app.route('/mine_block', methods=['GET'])
def mine_block():
   # get the data we need to create a block
   previous_block = blockchain.get_previous_block()
   previous_proof = previous_block['proof']
   proof = blockchain.proof_of_work(previous_proof)
   previous_hash = blockchain.hash(previous_block)

   block = blockchain.create_blockchain(proof, previous_hash)
   response = {'tx_data': 'Harriet sends 5 ethers to Elsie!',
               'index': block['index'],
               'timestamp': block['timestamp'],
               'proof': block['proof'],
               'previous_hash': block['previous_hash']}
   return response


@app.route('/get_blockchain', methods=['GET'])
def get_chain():
   response = {'chain': blockchain.chain,
               'length': len(blockchain.chain)}
   return response


# Check validity of blockchain
@app.route('/valid', methods=['GET'])
def valid():
    valid = blockchain.chain_valid(blockchain.chain)

    if valid:
        response = {'Is blockchain valid?': True}
    else:
        response = {'Is blockchain valid?': False}
    return response

if __name__ == "__main__":
    app.run(debug=True)




''
