a=int(input())
b=[int(a) for a in input().split()]
c=[int(a) for a in input().split()]
d=[x for x in b if x in c]
string=' '.join(str(e) for e in d)
print(string)
