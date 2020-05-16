
def f(n):
    sum1=0
    sum2=0
    for i in range(n+1):
        sum1=sum1+i*i
        sum2=sum2+i
    sum2=sum2*sum2
    print(sum2-sum1)

t=int(input())
for i in range(t):
    n=int(input())
    f(n)
