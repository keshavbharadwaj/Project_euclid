def numbers(n,x):
    n=str(n)
    consecutive=[]
    for i in range(len(n)-x+1):
        p=n[i:i+x]
        consecutive.append(p)
    max=0
    for i in consecutive:
        prod=1
        for j in i:
            prod=prod*int(j)
        if prod>max:
            max=prod
                
    print(max)


t=int(input())
for i in range(t):
    _,x=map(int,input().split())
    n=int(input())
    numbers(n,x)
