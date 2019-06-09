
#Let there Be a list adhoc
adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
li1=[]
li2=[]
for i in adhoc:
    if i<=2:
        li1.append(i)
    elif i>5:
        li2.append(i)
print("values less than or equal to 2:\n")
print(li1)
print("\nvalues greater than 5:\n")
print(li2)

