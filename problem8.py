#!/usr/bin/python3
#Run in Linux
import os
import subprocess
myfile=open("commands2.txt","w")
erfile=open("err.txt","w")
count=0
prirnt("Enter commands line by line and enter $$$ to end input")
comms=[]
while True:
	inc=input("Enter Next Command\n")
	if '$$$' in inc:
		break
	else:
		comms.append(inc)
		myfile.write(inc)
		myfile.write("\n")
myfile.close()
count=[]
dup=comms
for comm in comms:
	#result = subprocess.check_output(comm,shell=True,universal_newlines=True,stderr=)
	res=subprocess.getoutput(comm)
	erfile.write(str(res))
	erfile.write("\n")
	comcheck=comm+";echo $?;"
	rcheck=subprocess.getoutput(comcheck)
	if '\n0' in str(rcheck):
		print(str(res))
for comm in comms:
	lx=comm

	dup.remove(comm)
	if lx in dup:
		cerr="echo warning warning command "+str(lx)+ " is given multiple times please do not do so | festival --tts"
		subprocess.call(cerr,shell=True)
		
		
		
	
erfile.close()
