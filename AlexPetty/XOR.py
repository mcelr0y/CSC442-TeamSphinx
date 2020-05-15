########################
# Name: Alex Petty
# Date: 5/6/2020
# Made for python 2.7
########################
from sys import stdin, stdout

# Variable for the name of the key file
FILE = "key2"


def main():

    # save the inputed file as a bytearray
    cText = bytearray(stdin.read())
    # open the file named in FILE then read and save it as a bytearray
    key = bytearray(open(FILE, 'r').read())

    # find the size of the inputed File and Create an empty bytearry the size of the input
    size = len(cText)
    xored = bytearray(size)
    
    # For loop that Xors the inputed file bytes with the file that was specified in FILE
    # and save it to the new bytearray at the same index
    for i in range(size):
        xored[i] = cText[i] ^ key[i]
    
    # output the xored result of the 2 files
    stdout.write(xored)
    stdout.flush()

main()
