import math
def lcm(n,x):
    common=[]
    nfac=[]
    xfac=[]
    i=2
    while(n!=1 or x!=1):
        if n%i==0 and x%i==0:
            common.append(i)
            n=n//i
            x=x//i
        elif n%i==0:
            nfac.append(i)
            n=n//i
        elif x%i==0:
            xfac.append(i)
            x=x//i
        else:
            i=i+1
    lcm=1
    overall=common+nfac+xfac
    for i in overall:
        lcm=lcm*i
    return lcm


t=int(input())
for i in range(t):
    n=int(input())
    if n==1:
        print(1)
    elif n==2:
        print(2)
    else:
        k=2
        for i in range(3,n+1):
            k=lcm(k,i)
        print(k)
