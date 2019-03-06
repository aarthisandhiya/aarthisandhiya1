# your code goes her
chars=input()
c=[]
x=' '
for i in chars:
  count = chars.count(i)
  if count ==1:
    c.append(i)
for i in range(0,len(c)):
	c[0]=c[0].lower()
	break
s=' '.join(c)
print(s)
	
