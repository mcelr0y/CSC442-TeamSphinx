##################################
##Name:
##Date: 5/2/2020
##Python: 2.7
##Program: TimeLock
##################################

import datetime
from sys import stdin
import pytz
from hashlib import md5

#debug mode?
DEBUG = False
#set to True if on the challenge server
ON_SERVER  = False

#valid time interval
INTERVAL = 60

EPOCH_DATETIME = ""
MANUAL_DATETIME = datetime.date.today()
MANUAL_DATETIME = MANUAL_DATETIME.strftime("%Y %m %d %H %M %S")

#manual current datetime?
if(DEBUG == True):
    MANUAL_DATETIME = "2017 03 23 18 02 06"
    EPOCH_DATETIME = "2000 01 12 12 12 05"

if (EPOCH_DATETIME == ""):
    EPOCH_DATETIME = raw_input()
#sets date time
datetimeFormat = '%Y %m %d %H %M %S'
md = datetime.datetime.strptime(MANUAL_DATETIME, datetimeFormat) 
ed = datetime.datetime.strptime(EPOCH_DATETIME, datetimeFormat)

local = pytz.timezone("US/Central")
local_dt = local.localize(ed, is_dst=None)
local_dt2 = local.localize(md, is_dst=None)

#converts date time to UTC and find difference
md = local_dt2.astimezone(pytz.utc)
ed = local_dt.astimezone(pytz.utc)
diff = md - ed
TotalSeconds = diff.days*86400 + diff.seconds
if (DEBUG == True):
    print ed.strftime("%Y-%m-%d %H:%M:%S %Z%z")
    print md.strftime("%Y-%m-%d %H:%M:%S %Z%z")
    print "Total Seconds:{}".format(TotalSeconds)

#find time intervals
modSeconds = TotalSeconds
while (modSeconds % INTERVAL != 0):
    modSeconds = modSeconds - 1

if(DEBUG == True):
    print "Modulus Seconds:{}".format(modSeconds)

#hashes the time through md5
strMod = str(modSeconds)
first = md5(strMod)
xfirst = str(first.hexdigest())
second = md5(xfirst)
if(DEBUG == True):
    print "First: {}".format(first.hexdigest())
    print "Second: {}".format(second.hexdigest())

#Converts hashes to strings
codeHash = str(second.hexdigest())

hashLetters = filter(str.isalpha, codeHash)
hashNumbers = ''.join(i for i in codeHash if i.isdigit())



codeLetters = hashLetters[:2]
codeNumbers = hashNumbers[-2:]

#reverses final two numbers
Reverse = 0
Number = int(codeNumbers)
while(Number > 0):
    Reminder = Number %10
    Reverse = (Reverse *10) + Reminder
    Number = Number //10
codeNumbers = str(Reverse)

#Gives Final Code
code = codeLetters + codeNumbers 
print "Code: {}".format(code)


