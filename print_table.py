#This file will contain the functionality to print a table from a file
from report import *
from string import *
from ipprotoconvert import *

def displayTable():
    """This function lets the user open a packet log and display the data from that log on the terminal"""
    #open file
    input_file = open(raw_input("Type the file you would like to open.\n"), 'rU')
    #print table header
    print "\n\n  [+] ------------------------------- Macary Madness ------------------------------ [+]"
    print " {:4} | {:8} | {:16} | {:16} | {:8} | {:6} | {:8} ".format(" No.", 
    "Time", "Source IP", "Destination IP", "Protocol", "Length", "Information")
    #read data from file
    data = input_file.readlines()
    #loop through and display data read from file
    for y in range(len(data)):
        sourceData = data[y].split(' ')
        sourceIP = sourceData[5]
        destIP = sourceData[14]
        protocol = protoName(int(sourceData[8]))
        length = sourceData[6]
        info = sourceData[13]

        print (" {:4} | {:8} | {:16} | {:16} | {:8} | {:6} | {:8} ").format((y+1), (data[y][11:19]),sourceIP,
        destIP, protocol, length, info)
    #close file
    input_file.close()