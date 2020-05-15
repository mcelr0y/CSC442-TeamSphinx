# Ashley Palmer
# 05/05/2020
# Program 7: Steg
# This program implements both the bit and the byte method of storing and retrieving hidden data.
# Use Python 2

from sys import argv

SENTINEL = [0x0, 0xff, 0x0, 0x0, 0xff, 0x0]
# False for left to right, True for right to left
REVERSED = False

# for storing using the byte method
def storeBytes(W, H, offset, interval):
    for i in range(len(H)):
        W[offset] = H[i]
        offset += interval
    for j in range(len(SENTINEL)):
        W[offset] = SENTINEL[j]
        offset += interval
    return W

# for storing using the bit method
def storeBits(W, H, offset, interval):
    i = 0
    while (i < len(H)):
        for j in range(8):
            W[offset] &= 0b11111110
            W[offset] |= ((H[i] & 0b10000000) >> 7)
            H[i] = (H[i] << 1) & (0b11111111)
            offset += interval
        i+=1
    while (i < len(SENTINEL)):
        for j in range(8):
            W[offset] &= 0b11111110
            W[offset] |= ((SENTINEL[i] & 0b10000000) >> 7)
            SENTINEL[i] = (SENTINEL[i] << 1) & (0b11111111)
            offset += interval
        i+=1
    return W

def extractBits(W, offset, interval):
    H = bytearray()
    sentinelcount = 0
    while ((offset < len(W)) and (sentinelcount < len(SENTINEL))):
        b = 0
        for j in range (8):
            b |= (W[offset] & 0b00000001) #
            if (j < 7):
                b = (b << 1) & 0b11111111 #
                offset += interval
        #print "b" + str(b)
        # now check if it matches the next sentinel byte - if so, increment the counter
        if (b == SENTINEL[sentinelcount]):
            sentinelcount += 1
        #if it doesn't - we're not at the end yet!
        #and if the counter is greater than 0, set the counter equal to 0
        elif (sentinelcount > 0):
            sentinelcount = 0
        H.append(b)
        offset += interval
    return H

# for extracting using byte method
def extractBytes(W, offset, interval):
    H = bytearray()
    while (offset < len(W)):
        end = False
        b = W[offset]
        # now check if it matches the first sentinel byte - if so, check further
        if (b == SENTINEL[0]):
            for i in range(1, len(SENTINEL)):
                end = True
                check = W[offset + interval*i]
                # if one doesn't match, then break the for loop and we're not at the end
                if (check != SENTINEL[i]):
                    end = False
                    break
            # otherwise, we're at the end and it's time to return the hidden file 
            if (end):
                return H
        H.append(b)
        offset += interval

################ERROR HANDLING AND GETTING COMMAND LINE ARGUMENTS###################

# error handling function
def usagemessage():
    print "Usage: "
    print "python Steg.py -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]"
    print " -s\tstore"
    print " -r\tretrieve"
    print " -b\tbit mode"
    print " -B\tbyte mode"
    print " -o<val>\tset offest to <val> (default is 0)"
    print " -i<val>\tset interval to <val> (default is 1)"
    print " -w<val>\tset wrapper file to <val>"
    print " -h<val>\tset hidden file to <val>"
    exit(0)

if((argv[1] == "help") or (len(argv) not in [5, 6, 7])):
    usagemessage()

# now store the args in appropriate variables
#storage mode? otherwise retrieve mode
if(argv[1] == "-s"):
    STORAGE_MODE = True
elif(argv[1] == "-r"):
    STORAGE_MODE = False
else:
    print "The first argument should be the mode, -s to store and -r to retrieve."
    exit(0)
#bit mode? otherwise byte mode
if(argv[2] == "-b"):
    BIT_MODE = True
elif(argv[2] == "-B"):
    BIT_MODE = False
else:
    print "The second argument should be bit mode (-b) or byte mode (-B)" 
    exit(0)

#set default offset and interval values
OFFSET = 0
INTERVAL = 1
WRAPPER = None
HIDDEN = None

for i in range(3, len(argv)):
    #offset specified?
    if(argv[i][:2] == "-o"):
        OFFSET = int(argv[i][2:])
        #print OFFSET
    #interval specified?
    elif(argv[i][:2] == "-i"):
        INTERVAL = int(argv[i][2:])
        #print INTERVAL
    elif(argv[i][:2] == "-w"):
        WRAPPER = argv[i][2:]
        #print WRAPPER
    elif(argv[i][:2] == "-h"):
        HIDDEN = argv[i][2:]
        #print HIDDEN
    else:
        usagemessage()

#if this is storage mode, need a hidden file
if (STORAGE_MODE == True and HIDDEN == None):
    print "Please specify a hidden file for storage mode. Did you mean -r for retrieve mode?"
    exit(0)

#####################DONE ERROR HANDLING##########################

#get bytes from the file into a bytearray
fw = open(WRAPPER, 'rb')
wrapper_bytes = bytearray(fw.read())
fw.close()
if (STORAGE_MODE):
    fh = open(HIDDEN, 'rb')
    hidden_bytes = bytearray(fh.read())
    fh.close()

if (STORAGE_MODE and BIT_MODE):
    output = storeBits(wrapper_bytes, hidden_bytes, OFFSET, INTERVAL)
elif ((STORAGE_MODE == True) and (BIT_MODE == False)):
    output = storeBytes(wrapper_bytes, hidden_bytes, OFFSET, INTERVAL)
elif ((STORAGE_MODE == False) and (BIT_MODE == False)):
    output = extractBytes(wrapper_bytes, OFFSET, INTERVAL)
else:
    output = extractBits(wrapper_bytes, OFFSET, INTERVAL)
print(output)

