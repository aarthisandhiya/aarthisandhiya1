a=int(input())
a=str(a)
c=[]
for i in range(0,len(a)):
    c.append(a[i])
temp=c[0]
for i in range(0,len(c)):
    for j in range(0,len(c)):
        if c[i]>c[j]:
            temp=c[i] 
            c[i]=c[j]
            c[j]=temp
d=list(c)
print(''.join(d))
