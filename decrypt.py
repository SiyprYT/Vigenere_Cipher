#Tristan Le - 3/04/2025

def decryption(ciphertext, keyword):
    # Remove spaces and convert both ciphertext and keyword to lowercase for consistency
    ciphertext = ciphertext.replace(" ", "").lower()
    keyword = keyword.replace(" ", "").lower()
    
    plaintext = []  # List to store the decrypted characters
    keyword_index = 0  # Index to track the position in the keyword
    
    for char in ciphertext:
        # all it does is check if the current character is a letter
        if char.isalpha(): 
            shift = ord(keyword[keyword_index % len(keyword)]) - ord('a')  # Calculate the shift based on the keyword
            decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))  # Apply the reverse shift for letters
            plaintext.append(decrypted_char)  # Add the decrypted letter to the list
            keyword_index += 1  # Move to the next character in the keyword
        elif char.isdigit():  # If the character is a digit (0-9)
            shift = ord(keyword[keyword_index % len(keyword)]) - ord('a')  # Use the keyword for digit shift as well
            decrypted_char = chr(((ord(char) - ord('0') - shift) % 10) + ord('0'))  # Apply the reverse shift for numbers
            plaintext.append(decrypted_char)  # Add the decrypted digit to the list
            keyword_index += 1  # Move to the next character in the keyword
        else:
            # For non-alphabet and non-digit characters (like spaces or punctuation), keep unchanged
            plaintext.append(char)
    
    return ''.join(plaintext)  # Convert the list to a string and return the decrypted message