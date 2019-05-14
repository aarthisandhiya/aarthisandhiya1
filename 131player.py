a=int(input())
s=0
while a>0:
    rem=a%10
    a=a//10
    if rem%2==1:
        s=s+rem
        break
    
if s%2==0:
    print("E")
else:
    print("O")
