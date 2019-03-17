a=input()
c=[]
for i in a.split():
    c.append(i)
temp=''
for i in range(0,len(c)):
    if c[i]=='and':
        temp=c[i-i]
        c[i-1]=c[i+1]
        c[i+1]=temp
print(' '.join(c))
