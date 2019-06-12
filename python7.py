#!usr/bin/python3

#Python program that implements the "touch" command and its options through file handling
import os
import datetime
import time
choice=int(input("Enter an option from following:\n1.Create a new empty file\n2.create new empty multiple files\n3.Check whether a file is created or not\n4.Update access and modification time.\n5.update access and modification time of a file to that of another file\n"))
if choice==1:
    loc=input("Enter file name with path to create it\n")
    myfile=open(loc,"w")
    myfile.close()
elif choice==2:
    locs=[]
    num=int(input("Enter Number of new files to create"))
    for i in range(num):
        loc=input("Enter name of file "+str(i)+" with location\n")
        myfile=open(loc,"w")
        myfile.close()
elif choice==3:
    loc=input("Enter file name with path to check whether present or not\n")
    try:
        open(loc,"r")
        print("File Present")
    except:
        print("File not present")
elif choice==4:
    loc=input("Enter file name with path to change its modification and time to current time\n")
    os.utime(loc)

elif choice==5:
    lop=input("Enter File path from which upadated date and time is extracted\n")
    loc=input("Enter File path To Update date and time\n")

    os.utime(loc,(os.path.getmtime(lop),os.path.getmtime(lop)))
   
