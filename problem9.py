#!/usr/bin/python
'''this code does not use dict methods like sorted and 
   lambda expressions as i am still learning them 
   i'll create a new code when i'm done'''
mystr=input("Enter String")
if len(mystr)>500:
    mystr=mystr.s[0:500]

#character ____dict___defining_____
dichar={}
for i in mystr:
    if i in dichar:
        dichar[i]+=1
    else:
        dichar[i]=1
#word___dict___defining____
clis=list(dichar.values())
clis.sort(reverse=True)
dicwor={}
worlist=mystr.split(" ")
for i in worlist:
    if i in dicwor:
        dicwor[i]+=1
    else:
        dicwor[i]=1
print(dicwor)
slis=list(dicwor.values())
slis.sort(reverse=True)
print(slis)
liw=[]
for i in slis:
    for j in dicwor:
        if dicwor[j]==i:
            wpush=j+" number= "+str(dicwor[j])
            if wpush not in liw:
                liw.append(wpush)
lic=[]
for i in clis:
    for j in dichar:
        if dichar[j]==i:
            spush=j+" number= "+str(dichar[j])
            lic.append(spush)
for i in slis:
    for j in dicwor:
        if dicwor[j]==i:
            if i==1:
                dicwor[j]+=1
                i+=1
                lenw=len(j)
                if len(mystr)+lenw+1>=500:
                    mystr=mystr[0:500-len]+" "+j
                else:
                    mystr=mystr+" "+j
print(lic)
print(liw)
print("New String = ",end=" ")
print(mystr)
