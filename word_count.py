f=open("file.txt",'r')
x=f.read().split(' ')
f.close()
print("word count is:",len(x))
  
