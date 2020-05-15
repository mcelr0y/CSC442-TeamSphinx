##########################
# Name: Alex Petty
# Date: 5/6/2020
# Made for python 2.7
##########################
#
# Required to install pytz
#
###########################
import time
from datetime import datetime
from hashlib import md5

# Not with base python and need to install
import pytz # pip install pytz

from sys import stdin

# make a debug mode
DEBUG = False
# When debug is used this varable acts as sys time
SET = "2017 03 23 18 02 06"
# Sets the range of time that a code is valid
INTERVAL = 60


# Time zone variables
local = "America/Chicago" # the timezone your machine is set to
Epoch = "America/Chicago" # the timezone that the origin time is set to

# set time zone
tzl = pytz.timezone(local)
tze = pytz.timezone(Epoch)


def main():
    # Read the epoch time and make it an array
    epoch = stdin.read().rstrip("\n")
    epoch = epoch.split(" ")
    
    # set t1 as a datetime object using the epoch time
    t1 = datetime(int(epoch[0]),int(epoch[1]),int(epoch[2]),int(epoch[3]),int(epoch[4]),int(epoch[5]))
    # change the time from the local timezone to UTC
    t1 = tze.localize(t1, is_dst=None).astimezone(pytz.utc)

    # Debugging statement
    if DEBUG:
        print "Epoch (UTC): {}".format(t1)

    # when in debug have the sys time be the time in the var SET
    if DEBUG:
        Ctime = SET
        Ctime = Ctime.split(" ")
        t2 = datetime(int(Ctime[0]), int(Ctime[1]),int(Ctime[2]),int(Ctime[3]),int(Ctime[4]),int(Ctime[5]))
        t2 = tzl.localize(t2, is_dst=True).astimezone(pytz.utc)
        print "Current (UTC): {}\n".format(t2)
    # The normal opperation of the program
    else:
        # Get the current sys time
        t2 = datetime.now()
        # change the time from the local timezone to UTC
        t2 = tzl.localize(t2, is_dst=None).astimezone(pytz.utc)
    
    # Get the diffence in time from the sys and epoch times
    diff = t2 - t1
    # change from a datetime obj to a float in seconds
    sec = diff.total_seconds()
    # find the time elapsed from the begining of the current time interval
    adj = int(sec) % INTERVAL
    # calculate the begining of the current time interval
    sec = int(sec) - adj

    # Debug to show the current time for the set Interval
    if DEBUG:
        print "Seconds: {}\n".format(sec)
    
    # hash the elapsed time at the beginning of the current time interval using md5
    hashs = md5(str(int(sec))).hexdigest()

    # more debug
    if DEBUG:
        print "MD5 #1: {}".format(hashs)

    # hash the hash     
    hashs = md5(hashs).hexdigest()

    #even more debug
    if DEBUG:
        print "MD5 #2: {}".format(hashs)
    
    # set up a counter and empty string
    count = 0
    code = ""
    # for loop to find the first 2 charactes in the hash
    for i in hashs:
        if i.isalpha() and count != 2:
            count += 1
            code += i
        elif count >= 2:
            break
    
    # counter var and len for the for loop range
    count = 0
    j = len(hashs)
    # for loop that finds the last 2 occuring integers
    for i in range(len(hashs)):
        if hashs[j-i-1].isdigit() and count != 2:
            count += 1
            code += hashs[j-i-1]
        elif count >= 2:
            break
    
    # print the code
    print code








main()
