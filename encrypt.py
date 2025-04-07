#Tristan Le - 3/04/2025

def encryption(plainText, keyword):
    cipherText = []  # store characters
    keyword_index = 0  # track position of the thingy
    
    print("")
    print("")
    print("You chose to...")
    print(" ")
    print("███████╗███╗░░██╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗")
    print("██╔════╝████╗░██║██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝")
    print("█████╗░░██╔██╗██║██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░")
    print("██╔══╝░░██║╚████║██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░")
    print("███████╗██║░╚███║╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░")
    print("╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░")
    print(" ")
    #totally didnt steal this from the code i made 2 years ago for computer science.... would never do that...

    for char in plainText:
        key_char = keyword[keyword_index % len(keyword)]  # if user makes the keyword 3 letters but the message is more, it loops it till it is the same or sum sum
        
        if char.isalpha():  # is the character a letter?!?!?!?!?!?
            shift = ord(keyword[keyword_index % len(keyword)]) - ord('a')  # Calculate the shift based on the keyword
            encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))  # adds the encryption thing on character
            cipherText.append(encrypted_char)  # add character to list
            keyword_index += 1  # NEXT CHARACTER!
        elif char.isdigit():  # is the character a number?!?!?!?!?!?
            shift = ord(keyword[keyword_index % len(keyword)]) - ord('a')  # Use the keyword for digit shift as well
            encrypted_char = chr(((ord(char) - ord('0') + shift) % 10) + ord('0'))  # puts the encryption thingy on number
            cipherText.append(encrypted_char)  # add digit to the list
            keyword_index += 1  # Move to the next character in the keyword
        else:
            # if it isnt a letter or number, dont change
            cipherText.append(char)
    
    return ''.join(cipherText)  # turns the list into string. wow!
