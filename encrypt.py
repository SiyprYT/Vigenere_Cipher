#Tristan Le - 3/04/2025

def encryption(plaintext, keyword):
    # Remove spaces and convert both plaintext and keyword to lowercase for consistency
    plaintext = plaintext.replace(" ", "").lower()
    keyword = keyword.replace(" ", "").lower()
    
    ciphertext = []  # List to store the encrypted characters
    keyword_index = 0  # Index to track the position in the keyword
    
    for char in plaintext:
        if char.isalpha():  # If the character is a letter
            shift = ord(keyword[keyword_index % len(keyword)]) - ord('a')  # Calculate the shift based on the keyword
            encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))  # Apply the shift for letters
            ciphertext.append(encrypted_char)  # Add the encrypted letter to the list
            keyword_index += 1  # Move to the next character in the keyword
        elif char.isdigit():  # If the character is a digit (0-9)
            shift = ord(keyword[keyword_index % len(keyword)]) - ord('a')  # Use the keyword for digit shift as well
            encrypted_char = chr(((ord(char) - ord('0') + shift) % 10) + ord('0'))  # Apply the shift for numbers
            ciphertext.append(encrypted_char)  # Add the encrypted digit to the list
            keyword_index += 1  # Move to the next character in the keyword
        else:
            # For non-alphabet and non-digit characters (like spaces or punctuation), keep unchanged
            ciphertext.append(char)
    
    return ''.join(ciphertext)  # Convert the list to a string and return the encrypted message