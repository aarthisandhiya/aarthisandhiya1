s,y=map(int,input().split())
w=[int(s) for s in input().split()]
for i in range(0,len(w)):
	if w[i]==y:
		print("Yes")
		break
else:
	print("No")
