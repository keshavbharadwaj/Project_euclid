
def fibo(n):
    cur=1
    prev=0
    sum=0
    term=1
    while(term<n):
        if term%2==0:
            sum+=term
        term=cur+prev
        prev=cur
        cur=term
    print(sum)


t=int(input())
for i in range(t):
    n=int(input())
    fibo(n)
