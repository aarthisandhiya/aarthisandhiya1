a,b=map(int,input().split())
c=0
for i in range(0,a):
	if b**i==a:
		c=c+1
		break
if c>0:
	print("yes")
else:
	print("no")                       
