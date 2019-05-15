a,b=map(int,input().split())
count=0
c=[int(a) for a in input().split()]
for i in range(0,len(c)-1):
    for j in  range(1,len(c)):
        if c[i]+c[j]==b:
            count=count+1
            break
        break
if count>=1:
    print("yes")
else:
    print("no")
