a=int(input())
b=[int(a) for a in input().split()]
f=0 
s=[]
r=[]
for i in range(0,len(b)):
    f=f+b[i]
    s.append(f)
r=s[::-1]
f=0
y=[]
for i in range(0,len(b)):
    f=f+b[i]
    y.append(f)
for k in range(0,len(r)):
    for l in range(0,len(y)):
        if k==l:
            print(r[k]+y[l],end=" ")
    
