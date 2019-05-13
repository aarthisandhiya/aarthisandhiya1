a=int(input())
b=[int(a) for a in input().split()]
c=sorted(b)
for i in range(0,len(b)):
    for j in range(0,len(c)):
        if b[i]==c[j]:
            print(j+1,end=" ")
