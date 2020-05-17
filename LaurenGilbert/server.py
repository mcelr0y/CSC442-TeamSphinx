#LOCAL HOST SERVER CODE
import socket

from time import sleep

from binascii import hexlify

 

ZERO = 0.025

ONE = 0.1

 

# set the port for client connections
PORT = 3058
IP = "127.0.0.1"

 

# create the socket and bind it to the port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((IP, PORT))

 

# listen for clients

# this is a blocking call

s.listen(0)

 

# a client has connected!

c, addr = s.accept()

 

# set the message

msg = "But choose carefully because you'll stay in the job you pick for the rest of your life. The same job the rest of your life? I didn't know that. What's the difference? You'll be happy to know that bees, as a species, haven't had one day off in 27 million years. So you'll just work us to death? We'll sure try. I didn't know that. What's the difference? You'll be happy to know that bees, as a species, haven't had one day off in 27 million years. So you'll just work us to death? We'll sure try.\n"

 

covert = "In the middle of the night" + "EOF"

covert_bin = ""

for i in covert:

              covert_bin += bin(int(hexlify(i), 16))[2:].zfill(8)

 

 

# send the message, one letter at a time

n = 0

for i in msg:

              c.send(i)

              # delay a bit in between each letter

              if(covert_bin[n] == "0"):

                           sleep(ZERO)

              else:

                           sleep(ONE)

              n = (n + 1) % len(covert_bin)

 

# send EOF and close the connection to the client

c.send("EOF")

c.close()
