# we use the RSA algorithm
from Crypto.PublicKey import RSA


class keypair():

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






