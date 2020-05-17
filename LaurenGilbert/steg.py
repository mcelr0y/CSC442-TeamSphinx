###################################
#Name: Lauren Gilbert
#Date 5/8/2020
#Version: Python 2.7
#Notes: 
#Execution (Storage): python steg.py -(s) -(b/B) -o(offset value) -i(interval value) -w(wrapper file) -h(hidden file)
#Execution (Retrieval): python steg.py -(r) -(b/B) -o(offset value) -i(interval value) -w(wrapper file)
###################################

import sys

#constants show retrieval method has reached end of image or message 
SENTINEL = bytearray([0x00, 0xFF, 0x00, 0x00, 0xFF, 0x00])

#method to store a defined file's data within a wrapper
def store(method, wrapper, hidden, offset, interval):
    
    # byte method for storing
    if(method == 'B'):
        x = 0
        while(x < len(hidden)):
            wrapper[offset] = hidden[x]
            offset += interval
            x += 1
        
        x = 0
        while (x < len(SENTINEL)):
            wrapper[offset] = SENTINEL[x]
            offset += interval
            x += 1
    
    #bit method for storing
    elif(method == 'b'):
        j = 0
        while(j < len(hidden)):
            for k in range(0, 8):
                wrapper[offset] &= 254
                wrapper[offset] |= ((hidden[j] & 128) >> 7)
                hidden[j] = (hidden[j] << 1) & (2 ** 8 - 1)
                offset += interval
            
            j += 1
            
        j = 0
        while(j < len(SENTINEL)):
            for k in range(0, 8):
                wrapper[offset] &= 254
                wrapper[offset] |= ((SENTINEL[j] & 128) >> 7)
                SENTINEL[j] = (SENTINEL[j] << 1) & (2 ** 8 - 1)
                offset += interval
            
            j += 1
        
    return wrapper
                
#method to retrieve hidden data from a defined wrapper file 
def retrieve(method, wrapper, offset, interval):
    
    #byte array to contain bytes of the retrieved hidden file
    hidden = bytearray()
    
    #byte method for retrieving
    if(method == 'B'):
        biteArr = bytearray()
        
        for z in range(0, 6):
            biteArr.append(wrapper[offset])
            offset += interval
            
        while(offset < len(wrapper)):
            if(biteArr != SENTINEL):
                hidden.append(biteArr[0])
                biteArr = biteArr[1:]
                biteArr.append(wrapper[offset])
                offset += interval
            else:
                return hidden
    
    #bit method for retrieving
    elif(method == 'b'):
        bitArr = bytearray()
        
        for k in range(0, 6):
            b = 0
            for j in range(0, 8):
                b |= (wrapper[offset] & 1)
                if(j < 7):
                    b = (b << 1) & (2 ** 8 - 1)
                    offset += interval
                
            bitArr.append(b)
            offset += interval

        while(offset < len(wrapper)):
            if(bitArr != SENTINEL):
                b = 0
                hidden.append(bitArr[0])
                bitArr = bitArr[1:]
                for j in range(0, 8):
                    b |= (wrapper[offset] & 1)
                    if(j < 7):
                        b = (b << 1) & (2 ** 8 - 1)
                        offset += interval
                
                bitArr.append(b)
                offset += interval
                
            else:
                return hidden
                        

######## MAIN CODE ################

#gets 'r' or 's' from the command line
sR = sys.argv[1][1]
# gets bit 'b' or byte 'B' method from the command line
method = sys.argv[2][1]
#gets the offset value from the command line
offset = int(sys.argv[3][2:])
 
#check to see if interval and ifso it will get the given value and open the vile and set wrapper file 
if(sys.argv[4][:2] == '-i'):
    interval = int(sys.argv[4][2:])
    with open(sys.argv[5][2:], 'rb') as part:
        wrapper = part.read()
        wBytes = bytearray(wrapper)
    if(sR == 's'):
        with open(sys.argv[6][2:], 'rb') as piece:
            hidden = piece.read()
            hBytes = bytearray(hidden)
else:
    interval = 1
    with open(sys.argv[4][2:], 'rb') as part:
        wrapper = part.read()
        wBytes = bytearray(wrapper)
    if(sR == 's'):
        with open(sys.argv[5][2:], 'rb') as piece:
            hidden = piece.read()
            hBytes = bytearray(hidden)
            
#performs storing method and direct file to output           
if(sR == 's'):
    newWrap = store(method, wBytes, hBytes, offset, interval)
    #sys.stdout.buffer.write(newWrap)
    sys.stdout.write(newWrap)
    
#performs retrieving method and direct file to output
elif(sR == 'r'):
    newH = retrieve(method, wBytes, offset, interval)
    #sys.stdout.buffer.write(newH)
    sys.stdout.write(newH)
