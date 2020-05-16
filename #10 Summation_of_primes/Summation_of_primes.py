import math
def primefinder(n):
    sum=0
    summer=[0,0]
    prime=[True for i in range(n+1)]    
    p=2
    while(p*p<=n):
        if prime[p]==True:
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1
    for i in range(2,n+1):
        if prime[i]:
            sum=sum+i
            summer.append(sum)
        else:
            summer.append(sum)
    return summer
            




summer=primefinder(1000000)
t=int(input())
for i in range(t):
    n=int(input())
    print(summer[n])
    
