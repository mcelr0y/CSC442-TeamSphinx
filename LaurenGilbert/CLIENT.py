#Lauren Gilbert
#version 2.7.17
#CLIENT CODE

#imports
import socket
from sys import stdout
from time import time
from binascii import unhexlify

 

#enable output for debugging 
DEBUG = False

# set the server IP address and port
IP = "localhost"
PORT = 3058

 
#create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((IP, PORT))

 
ONE = 0.1
ZERO = 0.025

 

# receive data until EOF
data = s.recv(4096)
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
#get the covert message
covert = ""
i = 0
