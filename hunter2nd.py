a=int(input())
b=[int(a) for a in input().split()]
d=sorted(b)
s=d[::-1]
for i in s:
    print(i,end="")
