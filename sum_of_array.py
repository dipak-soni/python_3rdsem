def sum_array(list):
    count=0
    for x in range(0,len(list)+1,1):    # sum() method which is inbuilt can be used
        count+=x
    return count

print(sum_array([int(x) for x in input("Enter numbers separated by space:").split(' ')]))