a,k=map(int,input().split())
c=0
d=[]
q=[int(a) for a in input().split()]
for i in range(0,len(q)):
    if q[i]==k:
        print(k)
        break
else:
    for i in range(0,len(q)):
        if q[i]<k:
            d.append(q[i])
    print(max(d))
