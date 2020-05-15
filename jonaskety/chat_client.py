#!/usr/bin/env python2.7
#####
# Name: Jonas Kety
# Date: April 24, 2020
# Description: Chat (timing) Covert Channel decoder in Python 2
#####
# imports
import socket
from sys import stdout
from time import time
from binascii import unhexlify

# enables debugging output
DEBUG = False

# set the server's IP address and port
ip = "jeangourd.com"
port = 31337

# creating the timings needed to produce 1/0
ONE = 0.4
ZERO = 0.025
# binary message
covert_bin = ""

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# print that connection succeeded
print("[connected to the chat server]\n...")

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
	if (delta >= ONE):
		covert_bin += "1"
	else:
		covert_bin += "0"

	if (DEBUG):
		stdout.write(" {}\n".format(delta))
		stdout.flush()

# print the entire covert binary if debug is true
if (DEBUG):		
	print(covert_bin)

# convert the covert
covert = ""
i = 0
while (i < len(covert_bin)):
	# process one at a time
	b = covert_bin[i:i+8]
	# convert to ASCII
	n = int("0b{}".format(b), 2)
	try:
		covert += unhexlify("{0:x}".format(n))
	except TypeError:
		covert += "?"
	# stop at EOF
	i += 8

# close the connection to the server
s.close()

# print disconnection from chat server
print("...\n[disconnected from the chat server]")

# print the hidden message
print("---------------")
print("Hidden message: " + covert)
print("---------------")