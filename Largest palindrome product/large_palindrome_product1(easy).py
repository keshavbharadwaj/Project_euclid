import math

def ispali(x):
    x=str(x)
    if x==x[::-1]:
        return 1
    else:
        return 0

def maxpali():
    big=999
    small=100
    p=[]
    for i in range(big,small-1,-1):
        for j in range(big,small-1,-1):
            prod=i*j
            if(ispali(prod)):
                p.append(prod)
    p.sort(reverse=True)
    return p

val=maxpali()
t=int(input())
for j in range(t):
    n=int(input())
    for i in val:
        if i<n:
            print(i)
            break
    
              
