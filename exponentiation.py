def exponential(a,power):
    ans=1
    for x in range(1,power+1,1):
        ans*=a
    print(ans)
exponential(5,4)