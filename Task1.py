# Task 1: This is a test to make sure you can compile some
# code and complete a rudimentary task. Examples were taken
# from the documentation for pycryptodome.
# URL: https://www.pycryptodome.org/en/latest/src/examples.html#encrypt-data-with-aes

# *************************************************************************************

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256

# *************************************************************************************


# Function that gives an example of a simple AES encryption and decryption.
def aes_example():
    print("AES Example:")
    message = "Hello from Mars!"
    key = get_random_bytes(16)
    print("Key: ", key)

    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    print("Ciphertext: ", ciphertext)

    nonce = cipher.nonce
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    message = cipher.decrypt_and_verify(ciphertext, tag).decode()

    print("Plaintext: ", message)

# *************************************************************************************


# Function that gives an RSA example of a private and public key.
def rsa_example():
    print("RSA Example:")
    code = "Pierre"
    key = RSA.generate(2048)
    encrypted_key = key.export_key(passphrase=code, pkcs=8, protection="scryptAndAES128-CBC")

    print(encrypted_key)

    code = "Pierre"
    encoded_key = encrypted_key
    key = RSA.import_key(encoded_key, passphrase=code)

    print(key.publickey().export_key())

# *************************************************************************************

# Function that gives SHA-256 example displaying hash.
def sha_256_example():
    print("SHA-256 Example:")
    hash_1 = SHA256.new()
    hash_1.update(b'Greetings from Jupiter')
    print(hash_1.hexdigest())

# *************************************************************************************
