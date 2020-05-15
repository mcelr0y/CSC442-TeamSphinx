# Ashley Palmer
# 04/16/2020
# Program 4: Chat Timing Covert Channel (Client)
# Python 2
# This program connects to a specified chat timing server, displays the overt message being sent, and attempts to decode a covert message. 

import socket
from sys import stdout
from time import time
from binascii import unhexlify

# enables debugging output to help figure out what the value of 1 might be
DEBUG = False

# value of ONE - all other times will be taken as ZERO
ONE = .2

# set the server's IP address and port
ip = "138.47.102.67"
port = 33333

#initialize the covert binary
covert_bin = ""

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))
print("Connected successfully!")

# receive data until EOF
data = s.recv(4096)
while (data.rstrip("\n") != "EOF"):
	# output the data
    stdout.write(data)
    stdout.flush()
	# start the "timer", get more data, and end the "timer"
    t0 = time()
    data = s.recv(4096)
    t1 = time()
	# calculate the time delta (and output if debugging)
    delta = round(t1 - t0, 3)
    if (DEBUG):
        stdout.write(" {}\n".format(delta))
        stdout.flush()
    if (delta >= ONE-0.001):
        covert_bin += "1"
    else:
        covert_bin += "0"

# close the connection to the server
s.close()

# now convert the covert message to ascii
covert = ""
i = 0
while (i < len(covert_bin)):
    #process one byte at a time
    b = covert_bin[i:i+8]
    #convert to ascii
    n = int("0b{}".format(b), 2)
    try:
        covert += unhexlify("{0:x}".format(n))
    except TypeError:
        covert += "?"
    #stop at the string EOF
    if (covert[-3:] == "EOF"):
        covert = covert[:-3]
        break
    i += 8
print("Covert message: " + covert)
