a,b,c=map(int,input().split())
e=[]
d=[int(a) for a in input().split()]
for i in range(b-1,c):
    e.append(d[i])
print(min(e))
     
