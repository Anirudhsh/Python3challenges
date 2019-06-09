#!/usr/bin/python3
import time
nam=input("Please Enter Your Name: \n")
cuti=int(time.strftime("%H"))
if cuti>5 and cuti<11:
    print("Good Morning "+nam)
elif cuti>=11 and cuti<16:
    print("Good Afternoon "+nam)
elif cuti>=16 and cuti<21:
    print("Good Evening "+nam)
else:
    print("Good Night "+nam)

