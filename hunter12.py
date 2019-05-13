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
for i in range(0,len(newlist)):
    if i==b:
        y=len(newlist)
        print(newlist[y-b])




