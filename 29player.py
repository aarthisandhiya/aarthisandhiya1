a,b=map(int,input().split())
c=0
for i in range(a,b):
    for j in range(1,a):
        if i**2<b:
            c=c+1
print(c)
