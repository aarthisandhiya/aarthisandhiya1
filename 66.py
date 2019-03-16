a,b=map(int,input().split())
s=[int(a) for a in input().split()]
w=[]
for i in s:
    if s.count(i)==b:
        w.append(i)
q=list(w)
last=[]
for i in q:
    if i not in last:
        last.append(i)
print(' '.join(str(t) for t in last))
