
def numadd(l):
    carry=0
    sum=0
    for i in range(40):
        y=0
        for j in l:
            y+=int(j[i])
        y+=carry
        if y>10:
            carry=y//10
        else:
            carry=0
    #print(carry)
    for j in l:
        sum+=int(j[49:39:-1])
    sum+=carry
    while(len(str(sum))>10):
        sum=sum//10
    print(sum)            



    



n=int(input())
l=[]
for i in range(n):
    p=input()

    l.append(p[-1::-1])
#print(l)
numadd(l)
