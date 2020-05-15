########################
# Name: Alex Petty
# Date: 4/19/2020
# Description: Decodes a message based on the delays between sent characters
# Made for python 2.7
######################## 
# Get socket and time library
import socket
from sys import stdout
from time import time

# enables debugging output
DEBUG = False

# set definition for '0' for delays
ZERO = 0.03

# set the server's IP address and port
#IP = 'jeangourd.com'
#PORT = 31337
IP = "localhost"
PORT = 1337


# Define the decode function to convert binary to ASCII (from BinaryDecde w/ minor change)
def decode(binary):

    # Initalize the varibles text as a string and i for an index
    text = ""
    i = 0
    
    # while loop to convert binary to ascii
    while (i < len(binary)):

        # Make var byte 7 or 8 bits based on n
        byte = binary[i:i+8]
        # Find the base10 char of byte
        byte = int(byte, 2)
        # get the representing character
        char = chr(byte)
        # Check if byte is ascii is vaild
        if ((ord(char) >= 32) and (ord(char) <= 122)):
            # If it is add the ascii character of byte
            text += char
        else:
            # Else add ?
            text += '?'
        # increment i
        i += 8
    
    # Return text
    return text

# Function to connect to server and receive/display message and analyze delays (from website with minor change)
def getMsg():
    #create covert array
    covert = ''
    
    # create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the server
    s.connect((IP, PORT))

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
            # determine if delay is a '1' or '0'
            if (delta > ZERO):
                covert += '1'
            else:
                covert += '0'
            if (DEBUG):
                    stdout.write(" {}\n".format(delta))
                    stdout.flush()


    # close the connection to the server
    s.close()
    # return the covert binary from the delays
    return covert

# Begining of main function
def main():
    # get the covert message from the server decode it and then display
    covert = getMsg()
    msg = decode(covert)
    print
    print("Covert message: " + msg)
    

main()

