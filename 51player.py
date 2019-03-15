a=int(input())
s=[int(a) for a in input().split()]
s=list(s)
z=[]
for i in range(0,len(s)):
	val=s[i]
	i=i-1
	while i>=0:
		if val<s[i]:
			s[i+1]=s[i]
			s[i]=val
			i=i-1
		else:
			break
print(s[1])
