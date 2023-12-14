# program to calculate days between two dates
class Date:
    def __init__(self,dd,mm,yyyy):
        self.dd=dd
        self.mm=mm
        self.yyyy=yyyy

def check_leap(year):
    if year%400==0:
        return 1
    elif year%100==0:
        return 0
    elif year%4==0:
        return 1
    else:
        return 0

def leap_year(date1,date2):
    count=0
    for x in range(date1.yyyy,date2.yyyy+1,1):
        count+=check_leap(x)
    if (check_leap(date1.yyyy) and date1.mm>2):
        count-=1
    if (check_leap(date2.yyyy) and date2.mm<2) or (date2.mm==2 and date2.dd!=29):
        count-=1
    return count

l=[31,28,31,30,31,30,31,31,30,31,30,31]
def days(date1,date2):
    if date2.mm>=date1.mm:
        n1=(date2.yyyy-date1.yyyy)*365+leap_year(date1,date2)+date2.dd-date1.dd
        for x in range(date1.mm-1,date2.mm-1,1):
               n1+=l[x]
    else:
        n1 = (date2.yyyy - date1.yyyy-1) * 365 + leap_year(date1, date2)+date2.dd-date1.dd
        for x in range(date1.mm - 1,12 -1):
            n1 += l[x]
        for x in range(0,date2.mm,1):
            n1+=l[x]
    if n1<0:
        return "negative"
    return n1

def validation(date1,date2):
    if date1.mm==2 and date1.dd in range(1,29+check_leap(date1.yyyy),1) and date2.mm==2 and date2.dd in range(1,29+check_leap(date2.yyyy),1):
         return 1
    elif date1.mm==2 and date1.dd in range(1,29+check_leap(date1.yyyy),1) and date2.mm in [1,3,4,5,6,7,8,9,10,11,12] and date2.dd in range(1,32,1):
         return 1
    elif date1.mm in [1,3,4,5,6,7,8,9,10,11,12] and date1.dd in range(1,32,1) and date2.mm==2 and date2.dd in range(1,29+check_leap(date2.yyyy),1):
         return 1
    elif date1.mm in [1,3,4,5,6,7,8,9,10,11,12] and date1.dd in range(1,32,1) and date2.mm in [1,3,4,5,6,7,8,9,10,11,12] and date2.dd in range(1,32,1):
         return 1
    else:
        print("Error while processing:")
        return 0
try:
    l1=[ int(x) for x in input("Enter first date separated by slash=").split("/")]
    l2=[ int(x) for x in input("Enter second date separeted by slash=").split("/")]
    (a,b,c)=l1
    date1=Date(a,b,c)
    (a,b,c)=l2
    date2=Date(a,b,c)
    if validation(date1, date2):
        print(days(date1, date2),"days")
        #print("%.3f"%(days(date1,date2)/365),"years")
except:
    print("Input error")

input("(Enter to terminate)")
  
"""date1=Date(16,8,2010)
date2=Date(28,11,2023)
days(date1,date2)"""
