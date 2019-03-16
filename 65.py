a=int(input())
s=[int(a) for a in input().split()]
c=[]
for i in s:
    if i<a:
        c.append(i)
e=list(c)
print(' '.join(str(w) for w in e))
