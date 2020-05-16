import math

def pytriplets(N):
    ans=-1
    for a in range(N//3,1,-1):
        b=((N**2)-(2*N*a))//(2*(N-a))
        c=N-a-b
        if c**2==a**2+b**2:
            prod=a*b*c
            if prod>ans:
                ans=prod
                real1=a
                real2=b
                real3=c

    if ans==0:
        ans=-1
    print(int(ans))            

t=int(input())
for i in range(t):
    n=int(input())
    pytriplets(n)

