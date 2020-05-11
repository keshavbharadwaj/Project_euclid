import math

def isprime(i):
    if i<=1:
        return 1
    if i==2:
        return 0
    if i>2 and i%2==0:
        return 1
    limit=math.floor(math.sqrt(i))
    for j in range(3,1+limit,2):
        if i%j==0:
            return 1
    return 0



def primerange(n):
    prime=[True for i in range(n+1)]
    p=2
    while(p*p<=n):
        if(prime[p]==True):
            for i in range(p*2,n+1,p):
                prime[i]=False
        p+=1
    c=[]
    for p in range(2,n):
        if prime[p]:
            c.append(p)
    return c


def permutations(l,p,start):
    n=len(l)
    subset=[]
    if p==1:
        return [[l[i]] for i in range(start,n)]
    for i in range(start,n):
        j=permutations(l,p-1,i+1)
        for k in j:
            subset.append([l[i]]+k)
    return subset
                                
                        
            
l=primerange(3000)
k=permutations(l,3,0)
l3=[]
p=permutations(l,2,0)
l4=[]

for i in p:
    if isprime(sum(i))==0:
        l4.append(sum(i))
for i in(k):
    if isprime(sum(i))==0:
        l3.append(sum(i))





