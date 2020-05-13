import math
def prime(n):
    i=2
    while(n!=1):
        if n%i==0:
            n=n//i
        else:
            i=i+1
        if i>math.sqrt(n):
            i=n
            break
    print(i)
        


t=int(input())
for i in range(t):
    n=int(input())
    prime(n)

   
