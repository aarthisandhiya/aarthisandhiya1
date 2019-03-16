e,u=map(int,input().split())
s=[int(e) for e in input().split()]
r=[]
for i in s:
    if s.count(i)==u:
        r.append(i)
q=list(r)
last=[]
for i in q:
    if i not in last:
        last.append(i)
print(' '.join(str(t) for t in last))
