a,b=map(int,input().split())
e=[int(a) for a in input().split()]
c=[]
for i in e:
    if i<b:
        c.append(i)
r=list(c)
list1=list(r)
for index in range(1,len(list1)):
        value = list1[index]
        i = index-1
        while i>=0:
            if value < list1[i]:
                list1[i+1] = list1[i]
                list1[i] = value
                i -= 1
            else:
                break
print(' '.join(str(e) for e in list1))
