a=input()
a=list(a)
s=[]
for i in range(0,len(a)-1,2):
    j=i+1 
    temp=a[i]
    a[i]=a[j]
    a[j]=temp
    s.append(a[i])
    s.append(a[j])
for i in s:
    print(i,end="")
