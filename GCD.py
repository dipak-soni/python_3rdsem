def gcd(a,b):
        for y in range(a if a>=b else b+1,0,-1):
            if a%y==0 and b%y==0:
                print("GCD is:",y)
                break
gcd(int(input("Enter first number:")),int(input("Enter second number:")))