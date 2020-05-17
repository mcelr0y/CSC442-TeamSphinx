#version 2.7.17
#Lauren Gilbert

from sys import stdin

def decode(binary, n):
    text = ""
    i = 0
    while (i< len(binary)):
        byte = binary[i:i+n] #byte is string here
        byte = int(byte, 2) #convert the byte to a base 2 integer
        #text += chr(byte)
       
        if(byte == 8):
            text = text[:-1]
            i += n
        else:
            text += chr(byte)
            i += n
    return text


binary = stdin.read().rstrip("\n")
#text = binary;


if (len(binary) % 7 ==0): #if 7 bit
    text = decode(binary, 7)

    print ("7-bit:")
    #print("\n")
    print (text)

if(len(binary) % 8 == 0): #if divisable by 8
    text = decode(binary, 8) #convert to ascii values
    print ("8-bit:")
    print (text)

