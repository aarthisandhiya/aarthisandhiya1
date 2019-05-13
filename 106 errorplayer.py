a=int(input())
s=[]
b=[int(a) for a in input().split()]
for i in range(0,len(b)-1):
    for j in range(1,len(b)):
        if b[i]==b[j]:
            s.append(b[i])
            del(b[i])
        else:
            s.append(b[i])
for k in s:
    print(k,end=" ")
