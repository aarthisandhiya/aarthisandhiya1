a=int(input())
e=[int(a) for  a in input().split()]
for s in e:
    w=e.count(s)
    if w==1:
        print(s)
