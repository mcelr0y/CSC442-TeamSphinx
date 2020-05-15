# Ashley Palmer
# 05/04/2020
# Program 6 - XOR Crypto
# Description: This program reads a key from a file called key in the current directory, reads the plaintext/ciphertext from stdin, and sends generated output to stdout. 
# Programmed in Python 2

from sys import stdin, stdout

def byte_xor(text, key):
    return ''.join(chr(ord(t) ^ ord(k)) for t, k in zip(text, key))

text = stdin.read().rstrip("\n")
with open('key', 'r') as f:
    key = f.read()
output = byte_xor(text, key)
stdout.write(output)
