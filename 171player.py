a=input()
c=[]
for i in a.split():
    c.append(i)
temp=''
if len(c)==1 and c[0]=='and':
    print("and")
else:
    for i in range(0,len(c)):
        if c[i]=='and':
            temp=c[i-i]
            c[i-1]=c[i+1]
            c[i+1]=temp
    print(' '.join(c))
