a,b=map(int,input().split())
f=[int(a) for a in input().split()]
c=0
d=0
for i in f:
    c=c+1 
    if i==b:
        d=c
        break
print(d)
   
