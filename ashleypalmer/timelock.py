#use python 3

from sys import stdin
from datetime import datetime
import pytz
from hashlib import md5

#debug mode?
DEBUG = False

#valid time interval
INTERVAL = 60
#manual current datetime? set to empty string if you want to use the current system time
MANUAL_DATETIME = "2017 03 23 18 02 06"

#converts local times to UTC times, takes a time and its timezone
def localToUTC(original_datetime, original_timezone):
    local_timezone = pytz.timezone(original_timezone)
    naive_datetime = datetime.strptime(original_datetime, "%Y %m %d %H %M %S")
    local_datetime = local_timezone.localize(naive_datetime, is_dst=None)
    utc_datetime = local_datetime.astimezone(pytz.utc)
    return utc_datetime

#get epoch time in UTC
local_epoch = stdin.read().rstrip("\n")
epoch = localToUTC(local_epoch, "America/Chicago")
if(DEBUG):
    print("Epoch (UTC): {}".format(epoch))

#get current time in UTC
if(MANUAL_DATETIME == ""):
    #use current system time
    current = datetime.now(tz=pytz.utc)
else:
    #use manual time
    current = localToUTC(MANUAL_DATETIME, "America/Chicago")
if(DEBUG):
    print("Current (UTC): {}".format(current))

#time difference in seconds
delta = (current - epoch).total_seconds()
if(DEBUG):
    print("Seconds elapsed: {}".format(delta))

#but now we need to back it up to the interval
delta = int(delta - (delta % INTERVAL))
if(DEBUG):
    print("Beginning of interval: {}".format(delta))

#now 1st md5
hashbrowns = md5(str(delta).encode()).hexdigest()
if(DEBUG):
    print("MD5 #1: {}".format(hashbrowns))
#second md5
hashbrowns = md5(hashbrowns.encode()).hexdigest()
if(DEBUG):
    print("MD5 #2: {}".format(hashbrowns))

#now get the code - first two letters
code = ""
for char in hashbrowns:
    if(char.isalpha()):
        code += char
    if(len(code) == 2):
        break
#first two numbers in reversed hash
for char in reversed(hashbrowns):
    if(char.isdigit()):
        code += char
    if(len(code) == 4):
        break
print("Code: {}".format(code))
