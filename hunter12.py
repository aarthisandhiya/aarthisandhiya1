a,b=map(int,input().split())
q=[int(a) for a in input().split()]
newlist=[]
while q:
    minimum=q[0]
    for x in q:
        if x < minimum:
            minimum=x
    newlist.append(minimum)
    q.remove(minimum)
    
lowest=newlist[0]
y=len(newlist)
for i in range(0,len(newlist)):
    if i==b and b==y:
        print(lowest)
else:
    print(newlist[y-b])




