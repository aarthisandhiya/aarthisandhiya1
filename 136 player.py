a,b=map(int,input().split())
count=0
c=[int(a) for a in input().split()]
for i in range(0,len(c)):
    if c[i]==b:
        count=count+1 
if count==0:
    print("no")
else:
    print("yes",count)
