from web3 import Web3,HTTPProvider
import json
from Crypto.PublicKey import RSA
import qrcode

ganache_url = "http://127.0.0.1:7545"  # call the smart contract in the blockchain
web3 = Web3(Web3.HTTPProvider(ganache_url)) # instantiate web3 connection
print("web3 is connected:", web3.isConnected()) #confirm if ganache is connected

#set pre-funded account as sender.
web3.eth.defaultAccount = web3.eth.accounts[1] # defines the address index, which is 1, from where the sender works.

abi = json.loads('[{ "anonymous": false, "inputs":[{ "indexed": false, "internalType": "address", "name": "from", "type": "address" }, { "indexed": false, "internalType": "address", "name": "receiver", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" }, { "indexed": false, "internalType": "string", "name": "message", "type": "string" } ], "name": "Transfer", "type": "event" }, { "inputs": [ { "internalType": "address payable", "name": "receiver", "type": "address" }, { "internalType": "uint256", "name": "value", "type": "uint256" }, { "internalType": "string", "name": "signature", "type": "string" } ], "name": "createOperation", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "transfer", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function"}]')

bytecode ='608060405234801561001057600080fd5b50610791806100206000396000f3fe608060405234801561001057600080fd5b50600436106100365760003560e01c80637d20368d1461003b578063a9059cbb14610057575b600080fd5b61005560048036038101906100509190610361565b610087565b005b610071600480360381019061006c91906103d0565b6101f8565b60405161007e91906104d1565b60405180910390f35b600060405180608001604052803373ffffffffffffffffffffffffffffffffffffffff1681526020018573ffffffffffffffffffffffffffffffffffffffff16815260200184815260200183815250908060018154018082558091505060019003906000526020600020906004020160009091909190915060008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060208201518160010160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506040820151816002015560608201518160030190805190602001906101b392919061020f565b5050507fcd6e659e4c2e75c3bfe47fecaccf39aeb368116a0ee52afb532e07f6cba6c0d1338484846040516101eb9493929190610485565b60405180910390a1505050565b600061020483836101f8565b506001905092915050565b82805461021b90610630565b90600052602060002090601f01602090048101928261023d5760008555610284565b82601f1061025657805160ff1916838001178555610284565b82800160010185558215610284579182015b82811115610283578251825591602001919060010190610268565b5b5090506102919190610295565b5090565b5b808211156102ae576000816000905550600101610296565b5090565b60006102c56102c084610511565b6104ec565b9050828152602081018484840111156102e1576102e06106f6565b5b6102ec8482856105ee565b509392505050565b60008135905061030381610716565b92915050565b6000813590506103188161072d565b92915050565b600082601f830112610333576103326106f1565b5b81356103438482602086016102b2565b91505092915050565b60008135905061035b81610744565b92915050565b60008060006060848603121561037a57610379610700565b5b600061038886828701610309565b93505060206103998682870161034c565b925050604084013567ffffffffffffffff8111156103ba576103b96106fb565b5b6103c68682870161031e565b9150509250925092565b600080604083850312156103e7576103e6610700565b5b60006103f5858286016102f4565b92505060206104068582860161034c565b9150509250929050565b610419816105b8565b82525050565b6104288161055e565b82525050565b61043781610582565b82525050565b600061044882610542565b610452818561054d565b93506104628185602086016105fd565b61046b81610705565b840191505092915050565b61047f816105ae565b82525050565b600060808201905061049a600083018761041f565b6104a76020830186610410565b6104b46040830185610476565b81810360608301526104c6818461043d565b905095945050505050565b60006020820190506104e6600083018461042e565b92915050565b60006104f6610507565b90506105028282610662565b919050565b6000604051905090565b600067ffffffffffffffff82111561052c5761052b6106c2565b5b61053582610705565b9050602081019050919050565b600081519050919050565b600082825260208201905092915050565b60006105698261058e565b9050919050565b600061057b8261058e565b9050919050565b60008115159050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b60006105c3826105ca565b9050919050565b60006105d5826105dc565b9050919050565b60006105e78261058e565b9050919050565b82818337600083830152505050565b60005b8381101561061b578082015181840152602081019050610600565b8381111561062a576000848401525b50505050565b6000600282049050600182168061064857607f821691505b6020821081141561065c5761065b610693565b5b50919050565b61066b82610705565b810181811067ffffffffffffffff8211171561068a576106896106c2565b5b80604052505050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b600080fd5b600080fd5b600080fd5b600080fd5b6000601f19601f8301169050919050565b61071f8161055e565b811461072a57600080fd5b50565b61073681610570565b811461074157600080fd5b50565b61074d816105ae565b811461075857600080fd5b5056fea2646970667358221220d70c525376adadb8621e51475625790163cfa55fb7c5f960033f61bc2312365364736f6c63430008070033'

createOperation = web3.eth.contract(abi=abi, bytecode=bytecode) #calling the constructor or function in solidity
tx_hash = createOperation.constructor().transact()

# show details in operations receipt such from, to, value.
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
print("Operations class details:", tx_receipt)

#signature verification.
def verifyOperation():
        self.rsa_PrivateKey = self.rsa_KeyPair.getPrivate(); # class method for acquiring private key.
        self.rsa_PublicKey = self.rsa_KeyPair.getPublic();  # class method for acquiring public key.

rsa_length = 1024
key = RSA.generate(rsa_length) #cryptographic strength is linked to the length of RSA.
priv_key = key.exportKey("PEM")
pub_key = key.publickey().exportKey("PEM")

#print(priv_key)
print(pub_key)


#generate qrcode using public key.when qrcode is scanned, it displays the public key. This is for Certificate Management System.
generate_img = qrcode.make(pub_key)
generate_img.save('image.png')