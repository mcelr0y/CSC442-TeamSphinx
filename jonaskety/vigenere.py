#!/usr/bin/env python2.7
####
# Name: Jonas Kety
# Date: March 30, 2020
# Description: Vigenere cipher in python2
# Can be ran using either of the following:
# python vigenere.py -[e/d] [key]
# ./vigenere.py -[e/d] [key]
####

# imports
from sys import stdin, argv
# string will provide all the characters in the alphabet
import string

# these are all of our letters in lists
# lowerUPPER
alpha = string.ascii_letters

# key cleaner (in case of spaces)
def keyClean(key):
    key = key.split()
    key = "".join(key)
    return key

# create the final text
def finalize(text):
    final = ""
    for num in text:
        if isinstance(num, int):
            # using the alphabet indexes to align with the list indexes
            final += alpha[num]
        else:
            # for all non-alphabetical characters
            final += num[0]

    return final

# encryption function
def encrypt(ciphertext, key):
    cipher = []
    nonAlpha = 0

    # clean to remove unwanted spaces
    key = keyClean(key)
    keyLength = len(key)

    for i in range(len(ciphertext)):
        current = ciphertext[i]

        # check if it is part of the non-alphabetical characters, increment counter
        if (not (current in alpha)):
            cipher.append([current])
            nonAlpha += 1
        # encryption algorithm, straight from the notes
        # C = (P + K)
        else:
            index = ((alpha.index(ciphertext[i]) + alpha.index(key[((i-nonAlpha) % len(key))])) % 26)

            # due to the way the letter list is, increment by 26 to go to uppercase
            if current.isupper():
                index += 26

            cipher.append(index)

    print(finalize(cipher))

# decryption function
def decrypt(ciphertext, key):
    plain = []
    nonAlpha = 0

    # clean to remove unwanted spaces
    key = keyClean(key)
    keyLength = len(key)

    for i in range(len(ciphertext)):
        current = ciphertext[i]

        # check if it is part of the non-alphabetical characters, increment counter
        if (current not in alpha):
            plain.append([current])
            nonAlpha += 1
        # decryption algorithm, straight from the notes
        # P = (C - K)
        else:
            index = ((26 + alpha.index(current) - alpha.index(key[((i - nonAlpha) % keyLength)])) % 26)

            # due to the way the letter list is, increment by 26 to go to uppercase
            if current.isupper():
                index += 26

            plain.append(index)

    print(finalize(plain))

# ensure we are getting the arguments needed
if (len(argv) < 3):
    print("Invalid arguments (2 expected, {} provided)".format(len(argv)-1))
    print("Usage: python vigenere.py -[e/d] [key]")
    exit(0)

text = stdin.readline().rstrip("\n")

# get the mode and the key from arguments
mode = argv[1]
key = argv[2]

# mode check (like a vibe check, but for modes)
if (mode == "-e"):
    while(text):
        encrypt(text, key)
        text = stdin.readline().rstrip("\n")

elif (mode == "-d"):
    while(text):
        decrypt(text, key)
        text = stdin.readline().rstrip("\n")
else:
    print("Invalid mode, use -e for encryption or -d for decryption")