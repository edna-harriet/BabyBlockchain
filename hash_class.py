from Crypto.PublicKey import RSA
#from Crypto.Hash import SHA1
import hashlib

class hash():
    def toSHA1(self):
        self.sha1 = toSHA1();

    msg =b'Kenya is in Africa'  # b does encoding by converting the string message into bytes to be acceptable by hash function.
    hash = hashlib.sha1(msg) #hash is a one way function thus having an output value, the data used at the input cannot be determined.
    print("1. Encoded hash of the message:", hash) #returns encoded data
    print("2. Hexadecimal format of the hash:", hash.hexdigest()) # outputs encoded data in hexadecimal format.