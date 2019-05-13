a=int(input())
b=[int(a) for a in input().split()]
f=0 
for i in range(0,len(b)):
    f=f+b[i]
    print(f,end=" ")
