e=input()
e=int(e)
c=0
for i in range(2,e):
	if e%i==0:
		c=c+1
if c==0:
	print("no")
else:
	if c>1:
		print("yes")
