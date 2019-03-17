a=int(input())
s=[]
c=0
for i in range(0,a):
    e=input()
    s.append(e)
for i in s:
    for j in s:
        if i==j:
            c=c+1 
if c>1:
    print("yes")
else:
    print("no")
