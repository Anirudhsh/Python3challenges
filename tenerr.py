#!/usr/bin/python3
import os
import subprocess
myfile=open("commands.txt")
erfile=open("err.txt","w")
count=0

for comm in myfile:
	count+=1
	#result = subprocess.check_output(comm,shell=True,universal_newlines=True,stderr=)
	if int(subprocess.call(comm,shell=True,stderr=None))==0:
		print("RUN")
	else:
		cerr='echo "There is an error in command "'+str(count)+" | festival --tts"
		subprocess.call(cerr,shell=True)
		
	
	
