#!/usr/bin/python3
import googlesearch
import qrcode


que=input("enter seach:\n")
links=googlesearch.search(que,stop=3)
qrc=[]
count=0
for i in list(links):
    count+=1
    qt=qrcode.make(i)
    namei=("/var/www/html/qim"+str(count)+".png")
    qt.save(namei)
mypage=open("/var/www/html/qrs.html","w")
mypage.write("<html><h1>THE TOP 3 LINKS</h1>")
while count:
    namei=("qim"+str(count)+".png")
    mypage.write("For Link "+str(count)+":")
    mypage.write('<img src="'+namei+'"><br>')
    count-=1
mypage.write("</html>")
mypage.close()

