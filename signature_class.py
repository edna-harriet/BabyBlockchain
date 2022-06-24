from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA512
import binascii

class signature():

    def __init__(self, priv_key, pub_key):
        self.rsa_KeyPair = keyPair(keyPair.ALG_RSA);
        self.rsa_PrivateKey = self.rsa_KeyPair.getPrivate(); # class method for acquiring private key.
        self.rsa_PublicKey = self.rsa_KeyPair.getPublic();  # class method for acquiring public key.
        self.cipherRSA = Cipher.getInstance(Cipher.ALG_RSA_PKCS1);

    rsa_length = 1024
    key = RSA.generate(rsa_length) #cryptographic strength is linked to the length of RSA.
    priv_key = key.exportKey("PEM")
    pub_key = key.publickey().exportKey("PEM")

    print(priv_key)
    print(pub_key)

#RSA Sign the message
    def __init__(self,sign):
        self.rsa_Hash = SHA512.new(message);
        self.rsa_Signer = self.rsa_Signer.getSigner();
        self.rsa_Signature = self.rsa_Signature.getSignature();  # class method for acquiring signature.

    message = b'Kenya is in Africa'
    hash = SHA512.new(message) #hash is a one way function thus having an output value, the data used at the input cannot be determined.
    signer = PKCS115_SigScheme(key)
    signature = signer.sign(hash)
    print("Signature:", binascii.hexlify(signature))

# RSA verify the message

    def __init__(self, verify):
        self.rsa_Hash = SHA512.new(message);
        self.rsa_Verifier= self.rsa_Verifier.getVerifier();
    #verify the valid message.
    message = b'Kenya is in Africa'
    hash = SHA512.new(message)
    verifier = PKCS115_SigScheme(pub_key)#The recepient uses public key shared by sender to verify the received message.
    print("signature valid:", hash != verifier)# For condition to be TRUE, then the hashed value length and verifier value length should be different except the receipient recalculates to find original message.

    # Verify the invalid signature
    message = b'Kenya Africa'
    hash = SHA512.new(message)
    verifier = PKCS115_SigScheme(pub_key) # The recepient uses public key shared by sender to verify the received message.
    print("signature valid:", hash == verifier)





