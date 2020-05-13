import math
t=int(input())

for j in range(t):
    i=int(input())
    i=i-1
    s1=math.floor((i)/3)
    s2=math.floor((i)/5)
    s3=math.floor((i)/15)
    sum=s1*(s1+1)*3+s2*(s2+1)*5-s3*(s3+1)*15
    sum=sum//2
    print(sum)
