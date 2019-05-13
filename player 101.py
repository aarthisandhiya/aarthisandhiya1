a=int(input())
s=0
b=[int(a) for a in input().split()]
for i in range(1,len(b)):
    s=s+b[i]
print(s)
