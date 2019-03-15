a,b=map(str,input().split())
b=int(b)
if b>len(a):
    print(a)
else:
    c=a[:-b]
    d=a[b:len(a)]
    print(d+c)
