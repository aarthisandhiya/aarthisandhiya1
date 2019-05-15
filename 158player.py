a,b=map(int,input().split())
c=a*b 
d=bin(c)
print(d)
s=[]
for i in range(0,len(d)):
    if d[i]=="1":
        s.append(i-1)
print(s[1])
