###################################################################
#
#   Chris McElroy
#   CYEN 301
#   5/8/2020
#   XOR Crypto
#
#   Description:  A XOR cipher program that reads a cipher key from file and can 
#                 encrypt or decrypt inputs.
#
#   Python 2.7    python xor.py < [cipher] > [output]
###################################################################

import fileinput
import sys

# reads key file
keyFile = open('key', 'r')
key = keyFile.read()

# reads input file
text = sys.stdin.read()

#xor function
def xor(key, text):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(key, text))

# calls function and prints the result
print(xor(key, text))
