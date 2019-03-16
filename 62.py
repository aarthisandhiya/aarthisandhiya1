a=int(input())
c=0
e=[]
for i in range(1,a):
	if a%i==0 and (a//i)%2==1:
		if i>c:
			e.append(i)
print(e[0])
	
