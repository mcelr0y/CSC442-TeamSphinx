##########################################
# Ashley Palmer
# CSC 442
# Program 3: Fetch Covert Message
# This program decodes a covert message from the file permissions of a specified directory in an FTP server.
# Version: Python 3
##########################################

from ftplib import FTP

# your desired method: either the 7 bit encoding style (7) or the 10 bit encoding style (10)
METHOD = 10
if (METHOD not in [7, 10]):
    print("Invalid method. Use 7 for the 7-bit encoding style or 10 for the 10-bit encoding style.")

# FTP specfics - fill these with your specific IP, port, and folder of interest
IP = "138.47.99.163"
PORT = 21
USERNAME = "valkyrie"
PASSWORD = "readytoride"
FOLDER = "/FILES"

#binary decoder
def decode(binary, n): 
    text = ""
    i = 0
    while (i < len(binary)):
        byte = binary[i:i+n]
        byte = int(byte, 2)
        if (byte == 8):
            text = text [:-1]
        else: 
            text += chr(byte)
        i += n
    return text

# contents of the FOLDER
files = []
binary = ""

# connect to the FTP server and retrieve contents of FOLDER
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USERNAME, PASSWORD)
ftp.cwd(FOLDER)
ftp.dir(files.append)
ftp.quit()

#parse file listing
for row in files:
    row = row[:10]
    if (METHOD == 7):
        if (row[:3] != "---"):
            continue
        else:
            row = row[3:]
    for char in row:
        if (char == "-"):
            binary += "0"
        else:
            binary += "1"

#now decode
if (METHOD == 7):
    text = decode(binary, 7)
    print(text)
else:
    if (len(binary) % 7 == 0):
        text = decode(binary, 7)
        print("7-bit")
        print(text)
    if (len(binary) % 8 == 0):
        text = decode(binary, 8)
        print("8-bit")
        print(text)
    else:
        text = decode(binary, 7)
        print("While this one didn't divide evenly by 7 or 8, here's an attempt at a 7-bit result.")
        print(text)
