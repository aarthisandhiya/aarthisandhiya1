a,b=map(str,input().split())
b=int(b)
if b>len(a):
    print(a)
else:
    c=a[:-b]
    d=a[b-1:len(a)]
    print(d+c)
