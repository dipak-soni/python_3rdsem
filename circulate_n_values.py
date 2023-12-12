l=[1,2,3,4,5]
n=int(input("How many times do you want to circulate the list:"))
for x in range(1,n+1,1):
    a=l[0]
    del l[0]
    l.append(a)
print(l)