
t=int(input())
no=['','One ','Two ','Three ','Four ','Five ','Six ','Seven ','Eight ','Nine ','Ten ','Eleven ','Twelve ','Thirteen ','Fourteen ','Fifteen ','Sixteen ','Seventeen ','Eighteen ','Ninteen ']
tens=['Twenty ','Thirty ','Forty ','Fifty ','Sixty ','Seventy ','Eighty ','Ninety ']
pos=['','Hundred ','Thousand ','Million ','Billion ','Trillion ']

 
def printer(digit,p):
    k=''
    l=len(digit)
    d2=''
    d1=''
    if int(digit)==0:
        return 0
    if l==3:
        d2=digit[0]
        d1=digit[1]+digit[2]
    elif l==2:
        d1=digit[0]+digit[1]
    elif l==1:
        d1=digit[0]
    if d2!='' and d2!='0':
        k+=no[int(d2)]+pos[1]
    if int(d1)<20:
        k+=no[int(d1)]
    else:
        k+=tens[int(d1[0])-2]+no[int(d1[1])]
    k+=pos[p]
    print(k,end='')  

for i in range(t):
    n=input()
    n=n[-1::-1]
    if(int(n)==0):
        print("Zero",end="")
    k=len(n)
    
    b=''
    m=''
    t=''
    h=''
    
    if k>8:
        b=n[9:12]
    if k>5:
        m=n[6:9]
    if k>2:
        t=n[3:6]
    h=n[0:3]
    
    b=b[-1::-1]
    m=m[-1::-1]
    t=t[-1::-1]
    h=h[-1::-1]
  
    if b!='' and b!='00':
        printer(b,4)
    if m!='' and m!='000':
        printer(m,3)
    if t!='' and t!='000':
        printer(t,2)
    if h!='' and h!='000':
        printer(h,0)
    print('')

