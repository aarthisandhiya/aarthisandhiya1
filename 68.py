a=int(input())
e=[int(a) for a in input().split()]
counting=0
for i in e:
    t=e.count(i)
    if t>counting:
        counting=t   
print(counting)
    
