a,k=map(int,input().split())
c=0
q=[int(a) for a in input().split()]
for i in range(0,len(q)):
    if q[i]==k:
        c=c+1
if c>0:
    print("yes")
else:
    print("no")
