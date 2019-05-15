a=int(input())
s=0
b=[int(a) for a in input().split()]
for i in range(0,len(b)):
    if b[i]<0:
        s=s+b[i]
print(s)
