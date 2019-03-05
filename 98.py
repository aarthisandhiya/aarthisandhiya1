a=int(input())
c=[int(a) for a in input().split()]
for i in range(0,len(c)):
	if c[i]>c[i+1]:
		print(i)
