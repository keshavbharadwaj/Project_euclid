import math
p=[2]

def primes(n):
    i=p[-1]+1
    n=n-len(p)
    prime=i-1
    while(n!=0):
        flag=0
        if i%2==0:
            flag=1
        else:
            for j in range(3,math.floor(math.sqrt(i))+1,2):
                if i%j==0:
                    flag=1
                    break
        if flag==0:
            n-=1
            prime=i
            p.append(prime)
        i=i+1
    print(prime)

t=int(input())
for i in range(t):
    n=int(input())
    if len(p)>n-1:
        print(p[n-1])
    else:
        primes(n)
