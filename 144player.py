a=int(input())
b=[int(a) for a in input().split()]
for i in range(0,len(b)):
    j=i-1
    if b[i]%b[j]==0:
        print(b[i],end=" ")
        
