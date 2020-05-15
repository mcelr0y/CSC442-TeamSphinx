###############################
# Name: Alex Petty
# Date: 3/29/20
# Disciption: Can encript and decript Vigenere ciphers with a custom key 
# made for python 2.7
###############################
# Get the modulas needed
from sys import stdin
import sys # couldn't load argv separately on my machine

# Set up base alphabet as reference
ALPHA = "abcdefghijklmnopqrstuvwxyz"

# cipher function to encrypt and decrypt
def cipher(mode, key, message):
        
        # if block for encrypting
	if (mode == "-e"):
                
                # initialize varible j for an index and ciphertext as the end string
		j = 0
		ciphertext = ""

                # for loop to encrypt the message
		for i in range(len(message)):

                        # finds the index for the first character in the key
			n = ALPHA.find(key[j].lower())

                        # checks if char in message is in the alphabet
			if (str.isalpha(message[i])):

                                # If block to check for lower and upper case letters
				if (message[i].islower()):

                                        # Sum the indexes of the current message and key letter,
                                        # then mod by the length of the ALPHA string.
                                        # With the new index k, add the charcter in ALPHA at the index
                                        # k to the ciphertext string
					k = (n + ALPHA.find(message[i])) % 26
					ciphertext += ALPHA[k]
				else:

                                        # In case of upper case, make it lower case
                                        # to check ALPHA and make it upper case before adding it to
                                        # cipher text
					k = (n + ALPHA.find(message[i].lower())) % 26
					ciphertext += ALPHA[k].upper()
                                
                                # If block to cycle the index for the key
				if (j == (len(key) - 1)):
					j = 0
				else:
					j += 1
                        
                        # If the character isn't alphabetical then add it to ciphertext
			else:
				ciphertext += message[i]

		# Return the encrypted message
		return ciphertext
    
        # If block for decrypting
	else:

                # Initialize the variable j as an index and plaintext as a string
		j = 0
		plaintext = ""

                # For loop to decrypt the message
		for i in range(len(message)):

                         
                        # finds the index for the first character in the key
			n = ALPHA.find(key[j].lower())

                        
                        # checks if char in message is in the alphabet
			if (message[i].isalpha()):

                                # If block to check if upper o lower case
				if (message[i].islower()):

                                        # Subtracts the current index by the key's index and mods by 26
					k = (ALPHA.find(message[i])- n) % 26

                                        # adds the charcter at the new index to plaintext
					plaintext += ALPHA[k]

				else:

                                        # Makes lower case before checking against ALPHA and 
                                        # changes it to Upper case bfore adding to plaintext
					k = (ALPHA.find(message[i].lower()) - n) % 26
					plaintext += ALPHA[k].upper()

                                # if block for incrementing j for key
				if (j == (len(key) - 1)):
					j = 0
				else:
					j += 1
                        
                        # If char not in alphabet then add to plaintext
			else:
				plaintext += message[i]

                # return plaintext
		return plaintext
    
# Main statement
def main():

    # Error if command line has less than three arguments
    if (len(sys.argv) < 3):
        print "Please use correct syntax"
        print "Example: python VigenereCipher [-e or -d] [yourKey]"
    
    # Error if command line has more than three arguments
    elif (len(sys.argv) > 3):
        print "Please use correct syntax"
        print "Example: python VigenereCipher [-e or -d] [yourKey]"

    # checks if the second argument is either -e or -d 
    elif (sys.argv[1] == "-e" or sys.argv[1] == "-d"):

        # stores -e or -d to n
        # stores the key as key
        # initalizes newKey as an array
        n = sys.argv[1]
        key = sys.argv[2]
    	newKey = []
        
        # Generates the newKey by removing spaces and non alphabet characters
        for i in range(len(key)):
            if (key[i].isalpha() and key[i] != " "):
                newKey += key[i]
	
        # get input and stroe as text
        # send input to cipher function and print the results
        text = stdin.read().rstrip("\n")
        text = cipher(n, newKey, text)
        print text
            

    # Error if second command line argument is incorrrect
    else:
        print "Please use correct syntax"
        print "Example: python VigenereCipher [-e or -d] [yourKey]"

# Call main to run program
main()
