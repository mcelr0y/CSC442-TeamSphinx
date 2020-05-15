########################
# Name: Alex Petty
# Date: 3/31/2020
# Description: Translates file permissions into a message from a FTP server
# Made for python 2.7
########################
# Get ftp library
from ftplib import FTP

# Set the address port and directory of the covert message
IP = 'jeangourd.com'
port = 21
directory = '7/'

# Sets user and password for the ftp server
USER = "anonymous"
password = ""

# Sets the method of the message and initalizes the array fetch for the directory
METHOD = 7 # 7 is for the 7 bit covert message 10 is for the whole directory covert message
fetch = []

# Connect to the server, navigate to the directory you specified, save the directory, log out of the server
ftp = FTP()
ftp.connect(IP, port)
ftp.login(USER, password)
ftp.cwd(directory)
ftp.dir(fetch.append)
ftp.quit()

# initalizes the covert string
covert = ""

# defines the decode funtion (taken from the binary decoder program)
def decode(binary, n):
    
    # Initalize the varibles text as a string and i for an index
    text = ""
    i = 0

    # if the method it 10 then do both 8-bit and 7-bit translation (with recursion)
    if n == 10:
        print "7-bit:"
        n = 7
        print decode(binary, 7)
        print "8-bit:"
        # message is already divisable by 7, so change to be divisable by 8
        while(len(binary) % 8 != 0):
            binary += '0'
        n = 8
        

    # while loop to convert binary to ascii
    while (i < len(binary)):

        # Make var byte 7 or 8 bit
        byte = binary[i:i+n]
        # Find the base10 char of byte
        byte = int(byte, 2)

        # Check if byte is ascii for backspace
        if (byte != 8):
            # If not add the ascii character of byte
            text += chr(byte)
        else:
            # Else remove the end character of the string text
            text = text[:-1]

        # increment i
        i += n

    # Return text
    return text

# If statement block for 7 or 10 methods
if METHOD == 7:
    # nested for loops to only save leftmost 7 permissions from the directory
    for i in range(len(fetch)):
        if fetch[i][0:3] == '---':
            for j in range(0,10):      
                if j > 2:
                    covert += fetch[i][j]
    # convert '-' to 0 and everything else to 1
    covert = covert.replace('-','0')
    covert = covert.replace('r','1')
    covert = covert.replace('w','1')
    covert = covert.replace('x','1')
    
    # decode the message
    print decode(covert,7)

# the 10 method if block
elif METHOD == 10:
    # nested for loops to save all 10 charaters of the permissions
    for i in range(len(fetch)):
        for j in range(0,10):
            covert += fetch[i][j]
    # make sure the message is divisable by 7 (8-bit modification done in decode function)
    while (len(covert) % 7 != 0):
        covert += '0'
    
    # convert '-' with 0 and everything else with 1
    covert = covert.replace('-', '0')
    covert = covert.replace('r', '1')
    covert = covert.replace('w', '1') 
    covert = covert.replace('x', '1')
    covert = covert.replace('d', '1')

    # print the decoded message
    print decode(covert, 10)
