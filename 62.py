a=int(input())
c=0
e=[]
for i in range(2,a):
	if a%i==0:
		if i>c:
			e.append(i)
print(e[0])
	
