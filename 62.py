a=int(input())
c=0
e=[]
for i in range(1,a):
	if a%i==0 :
	    if (a//i)%2==1:
		    if i>c:
			    e.append(i)
	    else:
	       e.append(a)
print(e[0])
	
