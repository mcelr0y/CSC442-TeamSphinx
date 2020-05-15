###############################################################################
#Name: Thomas Mason
#Date:4/23/2020
#Description: Program that connects to a chat server and decodes hidden Message
###############################################################################
import socket
from sys import stdout
from time import time
from binascii import unhexlify

# enables debugging output
DEBUG = False

# set the server's IP address and port
ip = "localhost"
port = 1337

#Constants
ZERO = 0.020
ONE = 0.1

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# receive data until EOF
data = s.recv(4096)
string = ''
covert_bin = ""
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

# close the connection to the server
covert = ""
i = 0

#Converts Covert Binary String to Readable Message
while (i < len(covert_bin)):
    # process one byte at a time
    b = covert_bin[i:i + 8]
    # convert it to ASCII
    n = int("0b{}".format(b), 2)
    
    try:
        covert += unhexlify("{0:x}".format(n))
    except TypeError:
        covert += "3"
    #stop at the string "EOF"
    i += 8
    if(covert[-3:] == "EOF"):
        covert = covert[:-3]
        covert = "\nHidden message: " + covert
        break
print covert
s.close()

