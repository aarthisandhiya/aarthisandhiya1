b=input()
s=[]
d=[]
for i in range(0,len(b)):
    if b[i]=='a' or b[i]=='e'  or b[i]=='o' or b[i]=='u' or b[i]=='A' or b[i]=='E' or b[i]=='O' or b[i]=='U' or b[i]=='i' or b[i]=='I':    
        s.append(b[i])
    else:
        d.append(b[i])
c=s+d 
for i in range(0,len(c)):
    print(c[i],end="")
        
    
