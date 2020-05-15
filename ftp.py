############################################
#Name:Thomas Mason
#Date: 4/2/2020
#Description: Decodes message in ftp server
#Version: python 2
############################################


from ftplib import FTP 

#Constants
IP = "138.47.99.163"
PORT = 21
#FOLDER = "7"
#METHOD = 7
FOLDER = "10" 
METHOD = 10

#modifiable variables
contents = []
modifiedRow = ""
message  = ""

#Function to decode binary
def decode(binary, n):
    text = ""
    i = 0
    while (i < len(binary)):
        byte = binary [i:i+n]
        byte = int(byte, 2)
        #Fixes issue with backspace by actually removing the final character
        if (byte == 8):
            text = text[:-1]
        else:
            text += chr(byte)

        i += n

    return text

#Connects to FTP and get Required Data
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login()
ftp.cwd(FOLDER)
ftp.dir(contents.append)
ftp.quit()

#Decodes Data retrieved from FTP Server
for row in contents:
    row = row[:10].strip("\n")
    modifiedRow = ""
    for letter in row:
        if (letter == "-"):
            letter = "0"
            modifiedRow += letter
        else:
            letter = "1"
            modifiedRow += letter
    #Filters out Bad Data
    if (METHOD == 7):
        if (modifiedRow[:3].__contains__("1")==True):
            pass

        else:
            modifiedRow = modifiedRow[3:]
            modifiedRow = decode(modifiedRow, 7)
            message += modifiedRow
    if (METHOD == 10):
        message  += modifiedRow
#Used to fix broxen Message if 10 was decoded in For loop
if (METHOD == 10):
    message = decode(message, 7)
print message



