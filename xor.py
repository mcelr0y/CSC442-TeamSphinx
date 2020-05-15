#####################################
#Name:Thomas Mason
#Date:5/8/2020
#Description:
#####################################
import sys

#stores files in two bytearrays
cryptFile = sys.stdin.read()
key_file = "3d2fad84f4e4a738dff8c58af7bf0742"
f= open(key_file,"r")
contents = f.read()
conArray = bytearray(contents)
cryptArray = bytearray(cryptFile)
index = 0
string= ""
#xor the bytes in the two strings
for x in cryptArray:
    n = x ^ conArray[index]
    index += 1
    string += chr(n)

#print output
print string
