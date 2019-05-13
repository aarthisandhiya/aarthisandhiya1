a=int(input())
s=0
b=[int(a) for a in input().split()]
for i in range(0,len(b)-1):
    j=i+1
    if b[i]>b[j]:
        s=s+b[i]
    else:
        s=s+b[j]
print(s)
