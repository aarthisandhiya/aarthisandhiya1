a,b,c=map(int,input().split())
a=str(a)
u=[]
for i in range(b-1,len(a)):
    u.append(a[i])
for i in range(0,len(u)):
    if i==c:
        c=u[i]
print(c)
    
