###############
#Lauren Gilbert
#version:
#Program: Xor cipher program
#Date:
#Notes: Can have two possible inputs for xor
#if two bits same produce 0, if different produce 1
#input will wither be plain text or cipher text
#key is same size as input
#look up xor values and create buffer
#################

#imports
from sys import stdin, argv


#key file is in same directory as program we can do 
key_file = "key.bin"

#read key from file that we open through the program 
#read key from a file as binary data using bytearray
def get_bytes_from_file(key_file):
    return open(key_file, "rb").read()

#contents of the file ciphertext, XOR (decrypt) it with the contents of the file key, and send the resulting plaintext to stdout
def cipherdecode(text,key):
    ciphertext =
    encrypt_hex = ""
    key_itr=0
    for i in range(len(msg)):
        temp = ord(msg[i]) ^ ord(key[key_itr])
        encrypt_hex += hex(temp)[2:].fill(2)
        key_itr +=1
        if key_itr >= len(key):
            key_itr = 0
    print ("encrypted message: ()".format(encrypt_hex))




    

def cipherencode(text,key):
    pass


#read plaintext/ciphertext from command line(stdin), returns a byte string
text = sys.stdin.read()
#text = stdin.read().rstrip("\n")
m = argv[1]

#send generated output
#two possible inputs
if (m == "ciphertext"): print decode(text, key)

elif (m == "plaintext"): print function_name(text, key)
