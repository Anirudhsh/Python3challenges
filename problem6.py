#!usr/bin/python3

#Python program that implements the "cat" command and its options through file handling

choice=int(input("Enter an option from following:\n1.Print the data of a single file\n2.Print data of multiple files\n3.Create a new empty file\n4.Create a file and enter some data\n5.Append data to already created file\n6.Redirect Content of one file and append to an existing file\n"))
if choice==1:
    loc=input("Enter name of file with location\n")
    myfile1=open(loc,"r")
    print(myfile1.read())
    myfile1.close()
elif choice==2:
    locs=[]
    num=int(input("Enter Number of files to print"))
    for i in range(num):
        loc=input("Enter name of file "+str(i)+" with location\n")
        locs.append(loc)
    for lc in locs:
        myfile=open(lc,"r")
        print(myfile.read())
        myfile.close()
elif choice==3:
    loc=input("Enter file name with path to create it\n")
    myfile=open(loc,"w")
    myfile.close()
elif choice==4:
    loc=input("Enter file name with path to create it\n")
    myfile=open(loc,"w")
    print("Enter a $ to stop taking input and write to file")
    while True:
        data=input()
        if data.endswith("$"):
            myfile.write(data[:-1])
            break
        else:
            myfile.write(data)
        myfile.write("\n")
    myfile.close()
elif choice==5:
    loc=input("Enter file name with path to append data to it\n")
    myfile=open(loc,"a")
    print("Enter a $ to stop taking input and append to file")
    while True:
        data=input()
        if data.endswith("$"):
            myfile.write(data[:-1])
            break
        else:
            myfile.write(data)
        myfile.write("\n")
    myfile.close()
elif choice==6:
    locr=input("Enter file name with path to redirect data from\n")
    locw=input("Enter file name with path to append the data\n")
    myfiler=open(locr,"a+")
    myfiler.seek(0)
    myfilew=open(locw,"a")
    myfilew.write(myfiler.read())
    myfilew.close()
    myfiler.close()
