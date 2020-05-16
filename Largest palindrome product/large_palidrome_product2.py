import math
import logging,sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
def ispali(x):
    p=x
    reverse=0
    while p!=0:
        reverse=reverse*10+p%10
        p=int(p/10)
    if reverse==x:
        return 1
    else:
        return 0

def maxpali(N):
    N=N-1
    big=999
    small=100
    max_value=0
    first=0
    second=0
    if N>906609:
        print(906609)
        return 0
    

    for i in range(big,small-1,-1):
        div=math.floor(N//i)
        
        if div>i:
            break
        while(small<div):
            prod=i*div
            if ispali(prod):
                if prod>max_value:
                    max_value=prod
                    first=i
                    second=div
                small=div
                break
            div-=1
    print(max_value)
    return 0

t=int(input())
for j in range(t):
    n=int(input())
    maxpali(n)
    
              

