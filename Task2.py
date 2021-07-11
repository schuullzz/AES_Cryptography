# Task 2: Start by generating several files of different lengths (one of them very short, shorter than 128 bits),
# another at least 1MB. These can be generated by programs or manually created. Then, write a program to encrypt
# them using AES, with 128 and 256 bit keys. This key should be generated randomly, using a cryptographically secure
# random number generator.  Determine how many times you can encrypt and decrypt a particular file in a second. Make
# a calculation to determine what size of file you could decrypt in one second with various settings.

# *************************************************************************************

from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# *************************************************************************************


def encrypt_decrypt_128(file_name):
    print("Encryption and Decryption with 128-bit Key")
    new_file = file_name + ".txt"
    print("File: ", new_file)
    data = [0, 0]
    start = datetime.now()

    while(datetime.now() - start).seconds < 1:
        key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_EAX)

        file_in = open(new_file, 'r')
        sentence = ""

        while True:

            current_sentence = file_in.readline()
            sentence += current_sentence

            if not current_sentence:
                break
            else:
                sentence += current_sentence

        ciphertext, tag = cipher.encrypt_and_digest(sentence.encode())
        data[0] = data[0] + 1
        file_in.close()

        if(datetime.now() - start).seconds >= 1:
            break

        nonce = cipher.nonce
        cipher = AES.new(key, AES.MODE_EAX, nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag).decode()
        data[1] = data[1] + 1

    return data

# *************************************************************************************


def encrypt_decrypt_256(file_name):
    print("Encryption and Decryption with 256-bit Key")
    new_file = file_name + ".txt"
    print("File: ", new_file)
    data = [0, 0]
    start = datetime.now()

    while(datetime.now() - start).seconds < 1:
        key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_EAX)

        file_in = open(new_file, 'r')
        sentence = ""

        while True:

            current_sentence = file_in.readline()
            sentence += current_sentence

            if not current_sentence:
                break
            else:
                sentence += current_sentence

        ciphertext, tag = cipher.encrypt_and_digest(sentence.encode())
        data[0] = data[0] + 1
        file_in.close()

        if(datetime.now() - start).seconds >= 1:
            break

        nonce = cipher.nonce
        cipher = AES.new(key, AES.MODE_EAX, nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag).decode()
        data[1] = data[1] + 1

    return data

# *************************************************************************************
