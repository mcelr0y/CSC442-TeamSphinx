####
# Name: Jonas Kety
# Date: March 30, 2020
# Description: 7- or 8-bit ASCII binary decoder in python2
####

# imports
from sys import stdin

# the decoding function
def decode(binary, n):
    text = ""
    i = 0
    while (i < len(binary)):
        # convert to bytes
        byte = binary[i:i+n]
        # translate bytes
        byte = int(byte, 2)
        # add the decoded characters to the text string
        # check for the backspace, remove the last character if it is
        if byte == 8:
            text = text[:-1]
        else:
            text += chr(byte)
        i += n

    return text

# reading binary from input
binary = stdin.read().rstrip("\n")

# determining if 7- or 8-bit
if (len(binary)  % 7 == 0):
    text = decode(binary, 7)
    print(text)
if (len(binary)  % 8 == 0):
    text = decode(binary, 8)
    print(text)