#!/usr/bin/python3
#please run program in root
import subprocess
import os
num=int(input("enter number of users you want to make\n"))
print("Enter UserNames\n")
li=[]
i=0
while i<num:
    una=input("Enter user name for user "+str(i+1))
    if  not una.isalpha():
        print("enter username that only contains aplhabets\n")
        i-=1
    else:
        li.append(una)
    i+=1
for na in li:
        commp="hello"+na
        comf="useradd -p $(openssl passwd -1 "+commp+") "+na
        os.system(comf)
