a=int(input())
d=[int(a) for a in input().split()]
w=[]
for i in d:
    if i not in w:
        if d.count(i)>1:
            w.append(i)
temp=w[0]
for i in range(0,len(w)):
    for j in range(1 ,len(w)):
        if w[i]<temp:
            temp=w[i] 
            w[i]=w[j] 
            w[j]=temp
print(' '.join(str(e) for e in w ))
        
