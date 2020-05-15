#!/usr/bin/env python3
#####
# Name: Jonas Kety
# Date: May 8, 2020
# Description: Timelock program in Python 3. Creates a code based on UTC time differences between the epoch time and the machine time. Double MD5 hashing.
#####
# imports
from sys import stdin
from datetime import datetime
from hashlib import md5
import time as timelibrary

# debug
DEBUG = True

# valid time interval
INTERVAL = 60

# manual current datetime
MANUAL_DATETIME = ""

# functions
# convert to UTC
def convertUTC(time):
    time2 = timelibrary.strptime(time, '%Y %m %d %H %M %S')
    return int(timelibrary.mktime(time2))

# get the hex value
def getHex():
    # get epoch time from stdin
    # epoch is separate from epochTime for easier debug printing
    epoch = stdin.read().strip('\n')
    epochTime = convertUTC(epoch)

    # use custom time or not
    if (MANUAL_DATETIME != ""):
        # print if debug is enabled
        if (DEBUG):
            print("Current time: {}".format(MANUAL_DATETIME))
        sysTime = convertUTC(MANUAL_DATETIME)
    else:
        currTime = datetime.now()
        # print if debug is enabled
        if (DEBUG):
            print("Current time: {}".format(currTime))
        sysTime = convertUTC("{} {} {} {} {} {}".format(currTime.year, currTime.month, currTime.day, currTime.hour, currTime.minute, currTime.second))

    # calculate time difference
    timeDiff = sysTime - epochTime
    # convert to interval time
    timeAdjust = timeDiff % INTERVAL
    # simplify the time elapsed
    timeFinal = str(timeDiff - timeAdjust)

    # debug printing
    if (DEBUG):
        print("Epoch time: {}".format(epoch))
        print("Seconds: {}".format(timeDiff))
        print("Seconds: {}".format(timeFinal))

    # encode and change to md5
    timeHex = timeFinal.encode('utf-8')
    m = md5(timeHex).hexdigest()
    if (DEBUG):
        print("First hash: {}".format(m))
    # twice
    mHex = m.encode('utf-8')
    md5code = md5(mHex).hexdigest()
    if (DEBUG):
        print("Second hash: {}".format(md5code))
    
    # return the converted (twice) md5 code
    return md5code

# get the code from the hex
def getCode(hexText):
    # need 2 alpha and 2 nums
    CHARS = ""
    NUMS = ""

    # get the first two letters from a-f, starting left to right
    for t in hexText:
        # if the value is a letter, add it to the CHARS
        if (t.isalpha()):
            CHARS += t
            # once we get 2 letters, get out
            if (len(CHARS) >= 2):
                break
    
    # get the first two numbers from 0-9, starting right to left
    for i in range(len(hexText) -1, -1, -1):
        # if the value is NOT a letter, add it to the NUMS
        if (not hexText[i].isalpha()):
            NUMS += hexText[i]
            # once we get 2 nums, get out
            if (len(NUMS) >= 2):
                break
    
    # combine the two for the code
    code = CHARS + NUMS

    # ADDED FOR THE CHALLENGE
    # final character which is the last character
    code += hexText[31]
    
    # format the code differently depending on debug
    if (DEBUG):
        print("Code: {}".format(code))
    else:
        print(code)

# main part of the program
getCode(getHex())