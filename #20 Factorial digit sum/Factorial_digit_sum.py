t=int(input())
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
for i in range(t):
    n=int(input())
    f=fact(n)
    sum=0
    while(f!=0):
        sum=sum+f%10
        f=f//10
    print(sum)
