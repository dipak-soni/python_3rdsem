f1=open("source.txt",'r')
f2=open("target.txt",'w')
f2.write(f1.read())
f1.close()
f2.close()
print("file copied successfully")