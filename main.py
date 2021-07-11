# Timothy Schultz
# Professor Hauschild
# CS 4732
# 07/10/21

import Task1
import Task2

# *******************************************************************************

print("Project 2: Cryptography\n")

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
        Task2.encrypt_decrypt_128("Below128")
        # Task2.encrypt_decrypt_256()
        print("")
    elif answer == 3:
        break
    else:
        print("Incorrect option try again.\n")



