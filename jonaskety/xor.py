#!/usr/bin/env python3
#####
# Name: Jonas Kety
# Date: May 8, 2020
# Description: XOR program in Python 3. Takes a binary key file and a ciphertext/plaintext to encode/decode the file.
#####

# read key from file named key
# read plaintext/ciphertext from stdin
# send generated output to stdout

# imports
import sys

# read plaintext/ciphertext data from stdin as binary data
m = sys.stdin.buffer.read()

# read key file (name 'key') as binary data
# r = read, b = binary
k = open('key', 'rb').read()

# bytearray for the final message
b = bytearray()

# consider if key is shorter than message length
# need to loop around 
for i in range(len(m)):
    x = chr(int(((m[i]) ^ k[i % len(k)])))
    b.extend(map(ord, x))

# print to stdout
sys.stdout.buffer.write(b)