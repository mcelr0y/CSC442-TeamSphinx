################################
#Name:Thomas Mason
#Date: 3/25/2020
#Purpose: Binary Decoder
###############################
from sys import stdin

#decodes the binary message
def decode(binary, n):
    text = ""
    i = 0
    while (i < len(binary)):
        byte = binary [i:i+n]
        byte = int(byte, 2)
        #Fixes issue with backspace by actually removing the final character
        if (byte == 8):
            text = text[:-1]
        else:
            text += chr(byte)
    
        i += n
        
    return text
#reads user input
binary = stdin.read().rstrip("\n")

#decides whether it is 7 or 8 bit binary
if (len(binary) % 7 == 0): 
    text = decode(binary, 7)
    print "7-bit:"
    print text
if(len(binary) % 8 == 0):
    text = decode(binary, 8)
    print "8-bit"
    print text 


