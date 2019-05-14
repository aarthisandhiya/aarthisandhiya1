a=int(input())
w=bin(a)
s=[]
s=w[::-1]
for i in range(0,len(s)):
    if s[i]=="1":
        print(i+1)
        break
     
     
     
     
