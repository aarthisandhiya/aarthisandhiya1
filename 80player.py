a=int(input())
c=0
b=[int(a) for a in input().split()]
for index in range(1,len(b)):
    value = b[index]
    i = index-1
    while i>=0:
        if value < b[i]:
            b[i+1] = b[i]
            b[i] = value
            i -= 1
        else:
            break
c=b[1]-b[0]
print(c)
