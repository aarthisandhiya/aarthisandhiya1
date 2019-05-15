a,b=map(int,input().split())
c=a|b 
d=bin(c)
count=0
for i in range(0,len(d)):
    if d[i]=="1":
        count=count+1
print(count)
