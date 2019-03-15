a,b=map(int,input().split())
s=[int(a) for a in input().split()]
w=sum(s)
if w==b:
    print("yes")
else:
    print("no")
    
