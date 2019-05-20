n=int(input())
lis=list(map(int,input().split()))
t=[]
for i in lis:
    if lis.count(i)>1:
        t.append(i)
x=set(t)
if len(x)==0:
    print("unique")
else:
    print(*x)
