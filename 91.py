n=int(input())
x=n
k=[]
while (n>0):
    a=int(float(n%2))
    k.append(a)
    n=(n-a)/2
d=k[::-1]
print(''.join(str(e) for e in d))
