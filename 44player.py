a,b=map(str,input().split())
b=int(b)
length=len(a)
c=a[:-b]
d=a[b-1:len(a)]
print(d+c)
