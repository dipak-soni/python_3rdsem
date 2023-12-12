# distance between two points 
# distance=sqrt((x2-x1)^2+(y2-y1)^2)
import math
l1=input("Enter x1 and y1:").split(' ')
l2=input("Enter x2 and y2:").split(' ')
try:
   distance=math.sqrt((((int(l2[0]))-(int(l1[0])))**2)+(((int(l2[1]))-(int(l1[1])))**2))
   print("Distance is:%.2f"%distance)
except:
   print("Input only numbers")
