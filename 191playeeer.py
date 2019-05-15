a=int(input())
b=[int(a) for a in input().split()]
c=[int(a) for a in input().split()]
c=c[::-1]
count=0
for i in range(0,len(b)):
    if b[i]==c[i]:
        count=count+1 
if count==len(b):
    print("yes")
else:
    print("no")
