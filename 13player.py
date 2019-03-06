# your code goes her
a=int(input())
ans=0
while a>0:
	b=a%10
	ans=ans+b**2
	a=a//10
print(ans)
