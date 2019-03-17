a,b=map(int,input().split())
t=[int(a) for a in input().split()]
u=[int(b) for b in input().split()]
for i in u:
    t.append(i)
for index in range(1,len(t)):
    value = t[index]
    i = index-1
    while i>=0:
        if value < t[i]:
            t[i+1] = t[i]
            t[i] = value
            i -= 1
        else:
            break
print(' '.join(str(e) for e in t))
