##########################
# Name: Alex Petty
# Date 3/25/2020
# Discription: convert binary to ascii-7 or ascii-8
# written for python 2.7
##########################
# Import module stdin
from sys import stdin

# Define the decode function
def decode(binary, n):

    # Initalize the varibles text as a string and i for an index
    text = ""
    i = 0

    # while loop to convert binary to ascii
    while (i < len(binary)):

        # Make var byte 7 or 8 bits based on n
        byte = binary[i:i+n]
        # Find the base10 char of byte
        byte = int(byte, 2)

        # Check if byte is ascii for backspace
        if (byte != 8):
            # If not add the ascii character of byte
            text += chr(byte)
        else:
            # Else remove the end character of the string text
            text = text[:-1]

        # increment i
        i += n
    
    # Return text
    return text

# Define main statement
def main():

    # Get stdin and save to var binary
    binary = stdin.read().rstrip("\n")

    # If block to determine if 7 bits or 8 bits message
    if (len(binary) % 7 == 0):

        # If seven print 7-bit and send binary and 7 to the decode function
        # then print the return text
        print "7-bit:"
        text = decode(binary, 7)
        print text

    if (len(binary) % 8 == 0):
        # If eight print 8-bit and send binary and 8 to the decode function
        # then print the return text
        print "8-bit:"
        text = decode(binary, 8)
        print text



# call the main statement to run the program
main()

    
