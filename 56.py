a,b=map(str,input().split())
c=0
for i in range(1,len(a)):
	if a[i]==b:
		c=i+1
		if c>0:
			break
		break
print(c)
