#################################
# Ashley Palmer
# 25 March 2020
# Assignment 2 - Vigenere Cipher
# This program takes a mode (-e for encryption and -d for decryption) and a key
# at the command line, then reads plaintext or ciphertext from stdin, then
# outputs either ciphertext or plaintext to stdout. 
# Version - Python 3
#################################

from sys import stdin, argv

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def process(text, mode, key):
    output = ""
    #keycounter keeps track of where you are in the key
    keycounter = 0
    for p in text:
        index = charToAlphabetIndex(p)
        #if the character isn't in the alphabet
        if (index == -1):
            output += p
        else:
            #encrypt
            if (mode == "-e"):
                code = ((index + intkey[keycounter]) % len(ALPHABET))
            #decrypt
            else:
                code = ((index - intkey[keycounter] + len(ALPHABET)) % len(ALPHABET))

            if (p.islower()):
                output += ALPHABET[code].lower()
            else:
                output += ALPHABET[code]
                
            keycounter += 1
            keycounter = keycounter % len(key)
        
    return output

def charToAlphabetIndex(char):
    for i in range(len(ALPHABET)):
        if (char == ALPHABET[i]):
            return i
        elif (char.upper() == ALPHABET[i]):
            return i
    return -1

###### MAIN #######

#error handling
if (len(argv) != 3):
    print("Usage: python3 vigenere.py [mode] [key]")
    exit(0)
mode = argv[1]
if (mode not in ["-e", "-d"]):
    print("Modes are -e for encryption and -d for decryption.")
    exit(0)
key = argv[2]
text = stdin.read().rstrip("\n")

lines = text.splitlines()

#convert key in terms of alphabet index
intkey = []
for k in key:
    index = charToAlphabetIndex(k)
    if (index != -1):
        intkey.append(index)

#now generate the output
for line in lines:
    ciphertext = process(line, mode, intkey)
    print(ciphertext)
