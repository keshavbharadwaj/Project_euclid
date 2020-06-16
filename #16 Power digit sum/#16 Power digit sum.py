
import math

t=int(input())
for i in range(t):
    n=int(input())
    res=1
    sum=0
    for i in range(n):
        res*=2
    while res!=0:
        sum+=res%10
        res=res//10
    print(sum)
