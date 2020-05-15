#!/usr/bin/env python2.7
#####
# Name: Jonas Kety
# Date: April 3, 2020
# Description: FTP (storage) Covert Channel decoder in Python 2
# ***** ALL EDITS DURING THE CHALLENGE HAVE APPROPRIATE COMMENTS *****
#####
# imports
from ftplib import FTP

# DEBUG variable
DEBUG = False

# global variables (FTP Specifics)
IP = "jeangourd.com"
PORT = 8008
DIR = "/.secretstorage/.folder2/.howaboutonemore"

# username / password   # ADDED DURING CHALLENGE
USER = "valkyrie"
PASS = "chooseroftheslain"

# bit method, 7- or 10-bit
METHOD = 10

# switches the directory based on the METHOD specified if no directory is given:    # EDITED DURING CHALLENGE
if (DIR == ""):
    if (METHOD == 7):
        DIR = "7"
    else:
        DIR = "10"

# data retrieved from server
CONTENTS = []

# decoding function
#pulled from binary program
def decode(binary, n):
    text = ""
    i = 0
    while (i < len(binary)):
        # convert to bytes
        byte = binary[i:i+n]
        # translate bytes
        byte = int(byte, 2)
        # add the decoded characters to the text string
        # check for the backspace, remove the last character if it is
        if byte == 8:
            text = text[:-1]
        else:
            text += chr(byte)
        i += n

    return text

# retrieve contents function
# only need to get the permissons
def getContents():
    # change to the directory
    ftp.cwd(DIR)
    ftp.dir(CONTENTS.append)

    # change the data such that we only get the permissions
    for i in range(len(CONTENTS)):
        CONTENTS[i] = CONTENTS[i][0:10]
        i += 1

# convert the data to binary function
def convert(data):
    string = ""

    # change which lines we concatenate based on the METHOD specified
    # 7-bit METHOD
    if (METHOD == 7):
        for perm in data:
            # check to see if the first three permissions are not declared
            if perm[:3] == ('---'):
                for val in perm[3:]:
                    # if the value of the permission is '-', add a 0 to the string, else add a 1
                    if (val == '-'):
                        string += "0"
                    else:
                        string += "1"
    # 10-bit METHOD
    else:
        for perm in data:
            # skip the checking, concatenate all
            for val in perm:
                # if the value of the permission is '-', add a 0 to the string, else add a 1
                if (val == '-'):
                    string += "0"
                else:
                    string += "1"
    
    # debug, print binary string
    if (DEBUG):
        print string

    # decode and print the newly converted string
    if (len(string) % 7 == 0):
        print decode(string, 7)
    elif (len(string) % 8 == 0):
        print decode(string, 8)

### main ###
# connect to the specified FTP server, get contents, disconnect
ftp = FTP()
ftp.connect(IP,PORT)
ftp.login(USER, PASS)   # EDITED DURING CHALLENGE
getContents()
ftp.quit()

# debug, print all perms retrieved from server
if (DEBUG):
    # display file listing
    for row in CONTENTS:
        print row

# convert the covert (message)!
convert(CONTENTS)