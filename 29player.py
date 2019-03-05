a,b=map(int,input().split())
c=0
for i in range(a,b):
	if i**2<b:
		c=c+1
print(c)
