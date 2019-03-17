a=int(input())
f=[int(a) for a in input().split()]
temp=0
for i in f:
    if i>temp:
        temp=i
print(temp)
