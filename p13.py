a=int(input())
sq=0
while a>0:
	m=a%10
	sq=sq+m*m
	a=a//10
print(sq)
