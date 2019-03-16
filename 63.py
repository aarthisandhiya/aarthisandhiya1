a=int(input())
b=[int(a) for a in input().split()]
c=[int(a) for a in input().split()]
d=[x for x in b if x in c]
#d=list(dict.fromkeys(d))or the below can also used
s = []
for i in d:
       if i not in s:
          s.append(i)
string=' '.join(str(e) for e in s)
print(string)
