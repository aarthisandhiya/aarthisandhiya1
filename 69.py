a,b=map(int,input().split())
c=[int(a) for a in input().split()]
del(c[-(b):])
print(' '.join(str(e) for e in c))
