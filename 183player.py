a=int(input())
c=[]
d=[]
b=[int(a) for a in input().split()]
for i in range(0,len(b)):
    if b[i]==0:
        c.append(b[i])
    else:
        d.append(b[i])
e=[]
e=d+c
for i in range(0,len(e)):
    print(e[i],end=" ")
