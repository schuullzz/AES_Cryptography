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

def aes_example():
    print("AES Example:")
    message = "Hello from Mars!"
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    print("Ciphertext: ", ciphertext)

    file_out = open("encrypted.bin", "wb")
    [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
    file_out.close()

    file_in = open("encrypted.bin", "rb")
    nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]

    # let's assume that the key is somehow available again
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    message = cipher.decrypt_and_verify(ciphertext, tag).decode()

    print("Plaintext: ",message)

# *************************************************************************************


def rsa_example():
    print("RSA Example:")
    code = "Pierre"
    key = RSA.generate(2048)
    encrypted_key = key.export_key(passphrase=code, pkcs=8, protection="scryptAndAES128-CBC")

    file_out = open("rsa.bin", "wb")
    file_out.write(encrypted_key)
    file_out.close()

    print(key.public_key().export_key())

    code = "Pierre"
    encoded_key = open("rsa.bin", "rb").read()
    key = RSA.import_key(encoded_key, passphrase=code)

    print(key.publickey().export_key())

# *************************************************************************************


def sha_256_example():
    print("SHA-256 Example:")
    hash_1 = SHA256.new()
    hash_1.update(b'Greetings from Jupiter')
    print(hash_1.hexdigest())

# *************************************************************************************
