a=int(input())
t=[int(a) for a in input().split()]
d=sorted(t)
s=d[::-1]
for i in s:
    print(i,end="")
