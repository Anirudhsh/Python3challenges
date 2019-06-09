#!/usr/bin/python3
import googlesearch


#choice selector
while True:
    choice=input("Enter 1 for taking input from KeyBoard\nand 2 for taking input from voice:\n ")
    if choice=='1':
        que=input("enter seach:\n")
        break
    elif choice=='2':
        que=input("")
        break
    else:
        print("Wrong choice selected\nEnter choice from 1 or 2\n")

links=googlesearch.search(que,stop=10)
li=[i for i in links]
linkfile=open("mylinkfile.txt","w")
for i in li:
    linkfile.write(i)
    linkfile.write("\n")

