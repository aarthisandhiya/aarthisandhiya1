s=int(input())
lis=list(map(int,input().split()))
t=[]
for i in lis:
    if lis.count(i)>1:
        t.append(i)
r=set(t)
if len(r)==0:
    print("unique")
else:
    print(*r)
