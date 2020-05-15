#!/usr/bin/env python2.7
#####
# Name: Jonas Kety
# Date: May 8, 2020
# Description: Steg program in Python 2. Contains both bit and byte method. Includes offset and interval.
# NOTE: I did ask some of my teammates for advice since my bit method wasn't working in the beginning of the challenge, and they helped me a bit on it afterwards.
# Also the BYTE method for what worked in the challenge (-r -B -o2048 -i2 -wlifealert.bmp > cyber.jpeg) DOES NOT WORK.
#####
# imports
import sys

# variable defaults
OFFSET = 0
INTERVAL = 1
SENTINEL = [0, 255, 0, 0, 255, 0]
SENTINEL_LENGTH = len(SENTINEL)
# error message
ERROR = "Invalid usage:\nSteg.py -(s/r) -(b/B) -o<val> [-i<val>] -w<val> [-h<val>]"

# functions
# store file within another file
def store(WRAPPER, OFFSET, INTERVAL):

    # get the hidden file
    HIDDEN = hiddenFile()
    # change wrapper to a list for easy concatenations
    WRAPPER = list(WRAPPER)

    # byte method
    if (sys.argv[2] == "-B"):
        # this is from the notes
        # storing hidden file into the wrapper
        for i in range(len(HIDDEN)):
            WRAPPER[OFFSET] = HIDDEN[i]
            OFFSET += INTERVAL

        # storing sentinel into the wrapper
        for i in range(len(SENTINEL_LENGTH)):
            WRAPPER[OFFSET] = SENTINEL[i]
            OFFSET += INTERVAL
        
    # bit method
    elif (sys.argv[2] == "-b"):
        # this is from the notes
        # storing a bit at a time
        # change the least significant bits
        for i in range(SENTINEL_LENGTH):
            HIDDEN += chr(SENTINEL[i])
        
        ### Recieved help here from teammates after challenge ###
        HIDDEN = list(HIDDEN)
        for i in range(len(HIDDEN)):
            currH = ord(HIDDEN[i])
            # for each 
            for x in range(8):
                currW = ord(WRAPPER[OFFSET])
                currW &= 11111110
                currW |= ((currH & 10000000) >> 7)
                currH <<= 1
                # set value of wrapper at offset to the new character
                WRAPPER[OFFSET] = chr(currW)
                OFFSET += INTERVAL

    # print the results
    print("".join(WRAPPER))

# get file from another file
def retrieve(WRAPPER, OFFSET, INTERVAL):
    # need to keep hidden data
    HIDDEN = ""
    # track if found
    FOUND = False

    # byte method
    if (sys.argv[2] == "-B"):
        while (not FOUND and len(WRAPPER) > OFFSET):
            HIDDEN += WRAPPER[OFFSET]
            OFFSET += INTERVAL
            # check for sentinel once enough data has been found
            if (len(HIDDEN) >= SENTINEL_LENGTH):
                for i in range(SENTINEL_LENGTH):
                    # break if the digits don't match
                    if (ord(HIDDEN[i - SENTINEL_LENGTH]) != SENTINEL[i]):
                        break
                    # if all the digits match, clear the hidden data and set found
                    elif (i == SENTINEL_LENGTH - 1):
                        HIDDEN = HIDDEN[:-SENTINEL_LENGTH]
                        FOUND = True
    
    # bit method
    # from the notes
    ### Recieved a bit of help here from teammates after the challenge ###
    elif (sys.argv[2] == "-b"):
        while (not FOUND and len(WRAPPER) > OFFSET + 7):
            # this is basically the same as the byte method, just with bits!
            tmpBit = 0
            for i in range(8):
                bit = ord(WRAPPER[OFFSET]) & 1
                tmpBit |= bit
                if (i < 7):
                    tmpBit <<= 1
                OFFSET += INTERVAL
            HIDDEN += chr(tmpBit)
            # check for sentinel once enugh data has been found
            if (len(HIDDEN) >= SENTINEL_LENGTH):
                for i in range(SENTINEL_LENGTH):
                    # break if the digits don't match
                    if (ord(HIDDEN[i - SENTINEL_LENGTH]) != SENTINEL[i]):
                        break
                    # if all the digits match, clear the hidden data and set found
                    elif (i == SENTINEL_LENGTH - 1):
                        HIDDEN = HIDDEN[:-SENTINEL_LENGTH]
                        FOUND = True
    # print the results
    print(HIDDEN)

# i tried to make these not functions but that didn't work out
# so here we are with a lot of functions for arguments....
# store hidden file
def hiddenFile():
    # check from the back side since we could have a potential interval in the middle
    if (sys.argv[-1][:2] == "-h"):
        return open(sys.argv[-1][2:], 'rb').read()[:-1]
    else:
        print(ERROR)
        exit(0)

# store the wrapper file
def wrapperFile():
    # check from the back side since we could have a potential interval in the middle
    if (sys.argv[-1][:2] == "-w"):
        return open(sys.argv[-1][2:], 'rb').read()[:-1]
    # in-case we have a hidden file
    elif (sys.argv[-2][:2] == "-w"):
        return open(sys.argv[-2][2:], 'rb').read()[:-1]
    else:
        print(ERROR)
        exit(0)

# store the offset amount
def offsetAmt():
    if (sys.argv[3][:2] == "-o"):
        return int(sys.argv[3][2:])
    else:
        print(ERROR)
        exit(0)

def intervalAmt():
    if (sys.argv[4][:2] == "-i"):
        return int(sys.argv[4][2:])
    else:
        # this doesn't error out because we need a default anyways
        return 1

# main
# if we don't have the minimum arguments, error out
if (len(sys.argv) < 5):
    print(ERROR)
    exit(0)

# get wrapper file, offset amount, and interval amount (if specified)
WRAPPER = wrapperFile()
OFFSET = offsetAmt()
INTERVAL = intervalAmt()

# storage
if (sys.argv[1] == "-s"):
    store(WRAPPER, OFFSET, INTERVAL)
# retrieval
elif (sys.argv[1] == "-r"):
    retrieve(WRAPPER, OFFSET, INTERVAL)
# error if anything else
else:
    print(ERROR)
    exit(0)