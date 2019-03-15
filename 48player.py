a=int(input())
s=' '
for i in range(1,a+1):
    if a%i==0:
        if i%2==1:
            s=s+str(int(i))+' '
print(s.strip())
