a=int(input())
s=[]
c=0
for i in range(0,a):
    e=input()
    s.append(e)
for i in range(0,len(s)-1):
    j=i+1 
    if str(s[i])==str(s[j]):
        c=c+1 
if c>=1:
    print("yes")
else:
    print("no")
