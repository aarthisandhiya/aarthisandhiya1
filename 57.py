a,b=map(str,input().split())
for i in range(1,len(a)):
	if a[i]==b:
		s=a.count(b)
print(s)
