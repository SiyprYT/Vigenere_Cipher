#Tristan Le - 3/04/2025

from encrypt import encryption
from decrypt import decryption

print("")
print("")
print("")
print("")
print("This is some encryption thingy made by myself (Tristan Le) for:")
print("Year 12 Computer Science")
print("")
print("")
print("")
print("")

choice = input("Would you like to encrypt or decrypt a message? (e/d): ").lower()
    
# checks what the user put
if choice == 'e':
    message = input("Enter the message: ").lower()
    keyword = input("Enter the keyword/phrase: ").lower()
    encrypted_message = encryption(message, keyword)  # Encrypt the message
    print(f"Encrypted message: {encrypted_message}")
elif choice == 'd':
    message = input("Enter the message: ").lower()
    keyword = input("Enter the keyword/phrase: ").lower()
    decrypted_message = decryption(message, keyword)  # Decrypt the message
    print(f"Decrypted message: {decrypted_message}")
# RAHHHHHHHHHHHH PLEASE TYPE THE RIGHT THING DAMMIT
else:
    print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")