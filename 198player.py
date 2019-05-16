a=int(input())
b=[int(a) for a in input().split()]
f=min(b)
e=b.index(f)
g=max(b)
r=b.index(g)
print(abs(r-e))
