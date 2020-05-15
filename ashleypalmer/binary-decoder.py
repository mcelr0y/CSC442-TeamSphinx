#################################
# Ashley Palmer
# 24 March 2020
# Assignment 1 - Binary Decoder
# This program takes a string in binary and converts it to ascii text.
# Programmed in Python 3!
#################################

from sys import stdin
SHOW_BACKSPACES = False

def decode(binary, n):
    text = ""
    i = 0
    while (i < len(binary)):
        byte = binary[i:i+n]
        byte = int(byte, 2)
        if (byte == 8):
            if (SHOW_BACKSPACES):
                print(text)
                print("backspace character!")
            text = text [:-1]
        else: 
            text += chr(byte)
        i += n
    return text

binary = stdin.read().rstrip("\n")

if (len(binary) % 7 == 0):
    text = decode(binary, 7)
    print("7-bit")
    print(text)
if (len(binary) % 8 == 0):
    text = decode(binary, 8)
    print ("8-bit")
    print(text)

