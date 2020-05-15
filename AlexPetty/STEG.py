###########################
# Name: Alex Petty
# Date: 5/7/2020
# Made for python 2.7
###########################
from sys import argv, stdout

# Set up global variables for the Offset and Interval with defaults
# Have global strings Wrap and Hid as the wrap file and hide files 
# and an array for the sentinel bytes
OFFSET = 0
INTERVAL = 1
WRAP = ""
HID = ""
SENT = [0,255,0,0,255,0]

# Begining of the main function used to save information from the command line
def main():
    # require the minimum number of arguments or exit
    if len(argv) < 4:
        print "Incorrect Syntax: python STEG.py -(sr) -(dB) -o<val> [-i<val>] -w<val> [-h<val>]"
        exit(1)
    
    # prepare globals
    global OFFSET
    global INTERVAL
    global WRAP
    global HID

    # look through the command arguments and save data to the corispondinf globals
    for i in range(len(argv)):
        arg = argv[i]
        if (arg[:2] == "-o"):
            OFFSET = int(arg[2:])
        elif (arg[:2] == "-i"):
            INTERVAL = int(arg[2:])
        elif (arg[:2] == "-w"):
            WRAP = arg[2:]
        elif (arg[:2] == "-h"):
            HID = arg[2:]

    # if block based on the first argument and minimum required of arguments for each
    if argv[1] == "-s" and len(argv) >= 5:
        # call the store funtion
        store()
    elif argv[1] == "-r" and len(argv) >= 4:
        # call the retrieve funtion
        retrieve()
    else:
        # error if neither are called
        print "Incorrect Syntax: python STEG.py -(sr) -(dB) -o<val> [-i<val>] -w<val> [-h<val>]"


################################
# Begining of the Store function
################################
def store():
    # Open read and store the wrapper file and hidden files as byte arrays
    wrap = bytearray(open(WRAP, 'r').read())
    hid = bytearray(open(HID, 'r').read())

    # set the off variabel to the value of the global offset
    off = OFFSET

    # If block to check if Byte or Bit mode
    if argv[2] == "-B":

        # make an index var and set to 0
        i = 0
        # while the index is less that the length of the hidden file loop
        # this loop adds the hidden file bytes to the wrapper file
        while i < len(hid):
            # replace the byte of the wrapper at the index of the offset with the 
            # byte of the index "i" of the hidden file
            wrap[off] = hid[i]
            # increment the offset by the interval global and i by 1
            off += INTERVAL
            i += 1
        
        # while loop to add the sentinel bytes to the end of the hidden message/file
        i = 0
        while i < len(SENT):
            # replaces the byte of the wrapper with the bytes of the sentinel
            wrap[off] = SENT[i]
            #increment like th eloop above
            off += INTERVAL
            i += 1
            
    # bit if statement block        
    elif argv[2] == "-b":
        # while loop to store the hidden file in the wrapper using the bit method
        i = 0
        while i < len(hid):
            # loop through the bits of the current byte 
            for j in range(8):
                # mask and shift the bits of the wrapper to store the hidden file's bit in
                # the least significant bit
                wrap[off] &= 11111110
                wrap[off] |= ((hid[i] & 10000000) >> 7)
                hid[i] = (hid[i] << 1) & (2 ** 8 - 1)
                off += INTERVAL
            i += 1
        # while loop to store the bits of the sentienl byte sequence
        i = 0
        while i < len(SENT):
            # same masking and shifting of bits like the above code
            for j in range(8):
                wrap[off] &= 11111110
                wrap[off] |= ((SENT[i] & 10000000) >> 7)
                SENT[i] = (SENT[i] << 1) & (2 ** 8 - 1)
                off += INTERVAL
            i += 1


    # This opens the original wrapper in read write and then write over the contents with the
    # new bytearray that has the hidden file within it
    temp = open(WRAP, "r+")
    temp.seek(0)
    temp.truncate()
    temp.write(wrap)
    temp.close()





######################################
# Begining of the retrieve function
######################################
def retrieve():
    # open, read and save the wrapper file in a byte array and
    # make an empty bytearray
    wrap = bytearray(open(WRAP, 'r').read())
    hid = bytearray()

    # Set the variable off to the global OFFSET and make a check variable
    off = OFFSET
    check = 0

    # if block to check for B (byte) and b (bit) modes
    if argv[2] == "-B":
        # While loop to extract the 
        while off < len(wrap):
            # save the byte of the wrapper at index off to b
            b = wrap[off]
            # check if b is part of the sentinel sequence index check
            if b == SENT[check]:
                # if b is a part of the sentinel byte increment check by 1 and
                # still add b to the new array hid in case it isn't the sentinel sequence
                check += 1
                hid.append(b)
            else:
                # If b is not a part of the sentinel sequence then add b to the new
                # bytearray hid and reset the check index
                hid.append(b)
                check = 0

            # increment the off (offset) variable by the global INTERVAL
            off += INTERVAL
            # if check is 6 then the sentinel sequence was detected 
            if check == 6:
                # break out of loop when sentinel is found becuase hidden file has ended
                break

        # remove the last 6 bytes becuase they are the sentinel bytes
        hid = hid[:-6]

    # if block for the bit mode
    elif argv[2] == "-b":
        # loop to extract the hidden file using the bit method
        while off < len(wrap):
            # make variable to store bits
            b = 0
            # Loop thorugh the bits of the current byte
            for j in range(8):
                # save the least significant bit of the current wrapper byte to b
                b |= (wrap[off] & 00000001)
                if j < 7:
                    # prevent errors and add shift the bits 1 left
                    b = (b << 1) & (2 ** 8 - 1)
                    # increment off by the global INTERVAL
                    off += INTERVAL
            # Check if the byte b is part is part of the sentinel sequence at index check
            if b == SENT[check]:
                # if b is a part of the sentinel byte increment check by 1 and
                # still add b to the new array hid in case it isn't the sentinel sequence
                check += 1
                hid.append(b)
            else:
                # If b is not a part of the sentinel sequence then add b to the new
                # bytearray hid and reset the check index
                hid.append(b)
                check = 0

            # increment the off (offset) variable by the global INTERVAL
            off += INTERVAL
            # if check is 6 then the sentinel sequence was detected
            if check == 6:
                # break out of loop when sentinel is found becuase hidden file has ended
                break

        # remove the last 6 bytes becuase they are the sentinel bytes
        hid = hid[:-6]


    # output the hidden file thorugh stdout
    stdout.write(hid)
    stdout.flush()

main()
