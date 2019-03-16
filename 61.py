a,b=map(int,input().split())
s=[int(a) for a in input().split()]
c=0
for i in s:
    for j in s:
        if i+j==b:
            c=c+1 
if c>0:
    print("yes")
else:
    print("no")
