a=int(input())
b=[int(a) for a in input().split()]
f=0 
s=[]
r=[]
for i in range(0,len(b)):
    f=f+b[i]
    s.append(f)
r=s[::-1]
for j in range(0,len(r)):
    print(r[j],end=" ")
