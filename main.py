# Timothy Schultz
# Professor Hauschild
# CS 4732
# 07/10/21

# *************************************************************************************

import Task1
import Task2

# *************************************************************************************

print("Project 2: Cryptography\n")

# While statement that acts like a switch statement to display menu.
# Prompts user for choice.
while True:
    print("Select an option:")
    print("1. Task 1")
    print("2. Task 2")
    print("3. Quit\n")

    answer = int(input("Option: "))
    print("")

    if answer == 1:
        Task1.aes_example()
        print("")
        Task1.rsa_example()
        print("")
        Task1.sha_256_example()
        print("")
    elif answer == 2:
        data = Task2.encrypt_decrypt_128("Below128")
        print("Data Collected for Encryption and Decryption in one second:")
        print("Number of Encryptions: ", data[0])
        print("Number of Decryptions: ", data[1])
        print("Data Collected for just Decryption in one second:")
        print("Number of Decryptions: ", data[2])
        print("")
        data = Task2.encrypt_decrypt_128("The Rime of the Ancient Mariner")
        print("Data Collected for Encryption and Decryption in one second:")
        print("Number of Encryptions: ", data[0])
        print("Number of Decryptions: ", data[1])
        print("Data Collected for just Decryption in one second:")
        print("Number of Decryptions: ", data[2])
        print("")
        data = Task2.encrypt_decrypt_128("Greater1MB")
        print("Data Collected for Encryption and Decryption in one second:")
        print("Number of Encryptions: ", data[0])
        print("Number of Decryptions: ", data[1])
        print("Data Collected for just Decryption in one second:")
        print("Number of Decryptions: ", data[2])
        print("")
        data = Task2.encrypt_decrypt_256("Below128")
        print("Data Collected for Encryption and Decryption in one second:")
        print("Number of Encryptions: ", data[0])
        print("Number of Decryptions: ", data[1])
        print("Data Collected for just Decryption in one second:")
        print("Number of Decryptions: ", data[2])
        print("")
        data = Task2.encrypt_decrypt_256("The Rime of the Ancient Mariner")
        print("Data Collected for Encryption and Decryption in one second:")
        print("Number of Encryptions: ", data[0])
        print("Number of Decryptions: ", data[1])
        print("Data Collected for just Decryption in one second:")
        print("Number of Decryptions: ", data[2])
        print("")
        data = Task2.encrypt_decrypt_256("Greater1MB")
        print("Data Collected for Encryption and Decryption in one second:")
        print("Number of Encryptions: ", data[0])
        print("Number of Decryptions: ", data[1])
        print("Data Collected for just Decryption in one second:")
        print("Number of Decryptions: ", data[2])
        print("")
    elif answer == 3:
        break
    else:
        print("Incorrect option try again.\n")

# *************************************************************************************
