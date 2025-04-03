#Tristan Le - 3/04/2025

from encrypt import encryption
from decrypt import decryption

action = input("Would you like to encrypt or decrypt a message? (e/d): ").lower()
    
# Validate user input, only accept 'e' or 'd'
    
    
    # Ask for the message and the keyword/phrase
message = input("Enter the message: ")
keyword = input("Enter the keyword/phrase: ")
    
    # Perform encryption or decryption based on the user's choice
if action == 'e':
    encrypted_message = encryption(message, keyword)  # Encrypt the message
    print(f"Encrypted message: {encrypted_message}")
elif action == 'd':
    decrypted_message = decryption(message, keyword)  # Decrypt the message
    print(f"Decrypted message: {decrypted_message}")
else:
    print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")