grid=[]
def upanddown(l):
    ans=1
    for i in range(len(l)-3):
        for j in range(20):
            prod=l[i][j]*l[i+1][j]*l[i+2][j]*l[i+3][j]
            #print(l[i][j],l[i+1][j],l[i+2][j],l[i+3][j])
            if prod>ans:
                ans=prod
    return ans

def rightleft(l):
    ans=1
    for i in range(20):
        for j in range(len(l)-3):
            prod=l[i][j]*l[i][j+1]*l[i][j+2]*l[i][j+3]
            if prod>ans:
                ans=prod
    return ans

def diagonalleft(l):
    ans=1
    for i in range(len(l)-3):
        for j in range(len(l)-3):
            prod=l[i][j]*l[i+1][j+1]*l[i+2][j+2]*l[i+3][j+3]
            if prod>ans:
                ans=prod
    return ans
def diagonalright(l):
    ans=1
    for i in range(len(l)-1,3,-1):
        for j in range(len(l)-1,3,-1):
            prod=l[i][j]*l[i-1][j-1]*l[i-2][j-2]*l[i-3][j-3]
            if prod>ans:
                ans=prod
    return ans
def diagonal3(l):
    ans=1
    for i in range(len(l)-3):
        for j in range(len(l)-1,3,-1):
            prod=l[i][j]*l[i+1][j-1]*l[i+2][j-2]*l[i+3][j-3]
            if prod>ans:
                ans=prod
    return ans

def diagonal4(l):
    ans=1
    for i in range(len(l)-1,3,-1):
        for j in range(len(l)-3):
            prod=l[i][j]*l[i-1][j+1]*l[i-2][j+2]*l[i-3][j+3]
            if prod>ans:
                ans=prod
    return ans





for i in range(20):
    s=input()
    s=s.split(' ')
    s=[int(i) for i in s]
    grid.append(s)
ans1=upanddown(grid)
ans2=rightleft(grid)
ans3=diagonalleft(grid)
ans4=diagonalright(grid)
ans5=diagonal3(grid)
ans6=diagonal4(grid)
print(max(ans1,ans2,ans3,ans4,ans5,ans6))
