#!/usr/bin/python3
import time
nam=input("Enter Name")
age=int(input("Enter Your Age"))
curryear=time.strftime("%Y")
totyear=95-age+int(curryear)
print(nam+" will be 95 year old in "+str(totyear))
