#Lauren Gilbert
#version 2.7.17

#encrypt and decrypt using -e and -d 
#all done in command line
#to run go to documents type python and name.py -e MyKey or -d control d when done
#handle if no key?

import string

from sys import stdin, argv
lower = "abcdefghijklmnopqrstuvwxyz"

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

 

#function that will encrypt message 

def encrypt(plaintext, key):

    ciphertext = ""
    i=0
    message=0
    k=0
    p=0
    c=0

    #make all lowercase 
    key = key.lower()
    #remove extra whitespace in code
    key = key.replace(" ", "")

    #go through plaintext
    while (i < len(plaintext)):

        #encrypt all uppercase messages with uppercase
        if (plaintext[i].isupper()):
            if (message == len(key)): 
                message=0
            else: 
                message=message
            #find the position in the alphabet of k and p
            k = lower.index(key[message])
            p = upper.index(plaintext[i])
            #encrypt
            c = (k + p)%26
            ciphertext += str(upper[c])
            i+=1
            message+=1
 

        #if plaintext character is lowercase, encrypt with an lowercase character

        elif (plaintext[i].islower()):
            #key wrap around
            if (message == len(key)): 
                message=0
            else: 
                message=message
            #find the position in the alphabet of k and p
            k = lower.index(key[message])
            p = lower.index(plaintext[i])
            #encrypt
            c = (k + p)%26
            ciphertext += str(lower[c])
            i+=1
            message+=1

        #if character is a symbol (including spaces), add the symbol to the ciphertext and move on

        else:
            ciphertext += plaintext[i]
            i+=1

    return ciphertext

#function that will decrypt message 
def decrypt(ciphertext, key):
    plaintext = ""
    i=0
    message=0
    k=0
    p=0
    c=0
    #lowercase all characters in key and remove white spaces
    key = key.lower()
    key = key.replace(" ", "")
    #cycling through the plaintext
    while (i < len(ciphertext)):
        #if ciphertext character is uppercase, decrypt with an uppercase character
        if (ciphertext[i].isupper()):
            #key wrap around
            if (message == len(key)): 
                message=0
            else: 
                message=message
            #find the position in the alphabet of k and p
            k = lower.index(key[message])
            c = upper.index(ciphertext[i])
            #decrypt
            p = (26 + c - k)%26
            plaintext += str(upper[p])
            i+=1
            message+=1
 

        #if ciphertext character is lowercase, decrypt with an lowercase character

        elif (ciphertext[i].islower()):

            #key wrap around
            if (message == len(key)): 
                message=0
            else: 
                message=message
            #find the position in the alphabet of k and p
            k = lower.index(key[message])
            c = lower.index(ciphertext[i])
            #decrypt
            p = (26 + c - k)%26
            plaintext += str(lower[p])
            i+=1
            message+=1

        #if character is a symbol (including spaces), add the symbol to the plaintext and move on

        else:
            plaintext += ciphertext[i]
            i+=1
    return plaintext

    
#user inputs-e or -d as first argument
mode = argv[1]
#second argument is the key
key = argv[2]
#take the user input and strip the extra line
text = stdin.read().rstrip("\n")

 

if (mode == "-e"): 
    ciphertext=encrypt(text,key)
    print ciphertext

elif (mode == "-d"): 
    plaintext=decrypt(text, key)
    print plaintext


