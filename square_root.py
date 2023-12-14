def find_low_high(number):
    low=high=0
    for x in range(1,number,1):
        if x*x<number:
            low=x
    high=low+1
    return [low,high]

def square_root(number):
     if number<0:
         raise "Enter only positive number"
     x=find_low_high(number) if number>1 else [0,1]
     low=x[0]
     high=x[1]
     while low<=high:
        mid=(low+high)/2
        if mid*mid==number:
           print(mid)
           break
        elif mid*mid<number:
           low=mid+0.000001    
        else:
           high=mid-0.000001  
     else:
        print("square root is:%.2f"%mid)
                       
square_root(float(input("Enter a number:")))

"""
another method 
import math
print(sqrt(float(input("enter a number:"))))

"""

"""
another method
x=float(input("Enter a number:")**0.5
print(x)

"""
