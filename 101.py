a,b=map(str,input().split())
c=int(b)
d=""
def reverse(d):
    return d[::-1]
for i in range(len(a)-1,c+1,-1):
        d=d+a[i]
        rev=reverse(d)
print(rev)
