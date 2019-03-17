a=int(input())
r=[int(a) for a in input().split()]
c=0
for i in r:
    for j in r:
        if i<j:
            c=c+1 
print(c)
