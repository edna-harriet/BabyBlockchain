import hashlib

class Block:
    def __init__(self, block_id, previous_hash, transaction_list):
        self.block_id = block_id
        self.transaction_list = transaction_list
        self.previous_hash = previous_hash


        self.block_data = ("-".join(transaction_list) + "-" + previous_hash).encode() #concatenates transaction lists and hash value then encodes the value.
        self.block_hash = hashlib.sha1(self.block_data).hexdigest()


#create transactions made of simple strings.
t1 = "Harriet sends 5.7 ethers to Elsie"
t2 = "James sends 2.1 ethers to Sharon"
t3 = "Sharon sends 4.0 ethers to Bob"
t4 = "Bob sends 3.1 ethers to Allan"

#create block
genesis_block = Block(1, "", [t1,t2])

print("block id:", genesis_block.block_id)
print("block transaction:", genesis_block.block_data)
print("block hash:", genesis_block.block_hash)

second_block = Block(2,genesis_block.block_hash, [t3,t4])

print("block id:", second_block.block_id)
print("block transaction:", second_block.block_data)
print("block hash:", second_block.block_hash)





