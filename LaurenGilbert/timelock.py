######################################################
# Name: Lauren Gilbert
# Date: 05/8/2020
# Written in Python 3.7
#Notes: python timelock.py < file
#######################################################


from sys import stdin
import datetime
import pytz
import time
from hashlib import md5

 

#Debug mode
DEBUG = True

#Manual current datetime

#CURRENT = "2010 06 13 12 55 34"

#System current datetime
CURRENT = datetime.datetime.now()

 

#Epoch time from stdin
#will read from command line and strip off extra at end 
EPOCH = stdin.readline().rstrip("\n")

def timelock(current, epoch):
              #Naive datetime
              nc = current #if using realtime
              #nc = datetime.datetime.strptime(current, "%Y %m %d %H %M %S") #if using manual time
              ne = datetime.datetime.strptime(epoch, "%Y %m %d %H %M %S")
              #timezones
              utc = pytz.timezone('UTC')
              cdt = pytz.timezone('US/Central')
              #localize the naive
              current = cdt.localize(nc, is_dst=None).astimezone(utc)
              e_utc = cdt.localize(ne, is_dst=None).astimezone(utc)
              #Convert dates to seconds and find the difference
              t1 = time.mktime(current.timetuple())
              t2 = time.mktime(e_utc.timetuple())
              delta = int(t1-t2)

              #getting into the beginning of the 60 second interval
              while(delta % 60 != 0):
                           delta = delta - 1

              #convert to string and remove new line char
              delta = str(delta).strip()

              #MD5 1:
              MD1 = md5(delta).hexdigest()

              #MD5 2:
              MD2 = md5(MD1).hexdigest()

             
              #getting the first two letters
              letters = ""

              for char in MD2:
                           #comparing ascii values
                           if(ord(char) >= 97 and ord(char) <= 122):
                                         if (len(letters) < 2):
                                                       letters += char

 

              #getting the last two numbers                         
              numbers = ""
              reverse = MD2[::-1]
              for char in reverse:
                           #comparing ascii values
                           if(ord(char) >= 48 and ord(char) <= 57):
                                         if(len(numbers) < 2):
                                                       numbers += char
                         

              code = letters + numbers

              #debug mode

              if (DEBUG):

                print 'Current (UTC):' , current

                print 'Epoch (UTC):', e_utc

                print 'Seconds:',delta

                print 'MD5 #1',MD1

                print 'MD5 #1',MD2

                print letters

 

              print 'Code:',code

 

timelock(CURRENT, EPOCH)
