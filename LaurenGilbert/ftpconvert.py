#############################################
#lauren gilbert
#Program 3: FTP Covert Channel
#version 2.7.17
#Notes:good codeing style = constants capitalized
#############################################

from ftplib import FTP

#method
METHOD = 10

#globals(FTP specifics) 

#FTP specifics
#this ip by default can be changed
IP = "jeangourd.com"
#port by default
PORT = 8008
#goes into folder and looks at files using 7 bit method
FOLDER = "/.secretstorage/.folder2/.howaboutonemore"
#allow to read binary and folder in binary 
use_passive=True
USER = "valkyrie"
PASS = "chooseroftheslain"
# Contents of the folder
contents = []

#authorizations
allow = []

# 7 and 8-bit binary strings
binary7 = ""
binary8 = ""

#connect to FTP server and fetch a file listing

#create ftp object
ftp = FTP()
#connect to ip on this port
ftp.connect(IP, PORT)
#anon login
ftp.login(USER,PASS)
#use cap t for boolean
ftp.set_pasv(True)
#change directory to folder
ftp.cwd(FOLDER)
#do a directory of folder
ftp.dir(contents.append)
#close folder
ftp.quit()

 

#Binary decoding function (code from cipher program)

def decode(binary, n):
    text = ""
    i = 0
    while (i < len(binary)):

        byte = binary[i:i+n]
        byte = int(byte, 2)
        #if backspace, remove last character of string
        if(byte == 8):
            text = text[:-1]
            i+=n
        else:
            text += chr(byte)
            i += n
    return text

 

#implement method 7

if (METHOD == 7):
    ##display file listing organize the output into rows
    for row in contents:
        #remove files that do not matter/add valuable files authrization list 
        if (row[0:3] == "---"):
            allow.append(row[3:10])
    #convert authorization to binary 
    i=0

    while (i < len(allow)):
        j=0
        while (j < len(allow[i])):
            if (allow[i][j] == "-"):
                binary7 += "0"
            else:
                binary7 += "1"
            j+=1
        i+=1

    #decode binary 7
    print decode(binary7,7)

       

# method 10 

if (METHOD == 10):
    #display file listing organize the output into rows for authorizations
    for row in contents:
        allow.append(row[0:10])

    #convert authorizations to binary and then add them to the binary list
    i=0
    while (i < len(allow)):
        j=0
        while (j < len(allow[i])):
            if (allow[i][j] == "-"):
                binary7 += "0"
            else:
                binary7 += "1"
            j+=1
        i+=1
        binary8 = binary7

    #will add extra 0's if 7bit can't be grouped into even bits
    if (((len(binary7)) % 7) != 0):
        binary7 += "0"

 
    #will add extra 0's if 8bit can't be grouped into even bits
    if (((len(binary8)) % 8) != 0):
        binary8 += "0"

    #print the 7 and 8-bit version of the message, one will be stupid

    print "7-bit: " + decode(binary7,7)

    print "8-bit: " + decode(binary8,8)
