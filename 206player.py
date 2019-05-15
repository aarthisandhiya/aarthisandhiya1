a=input()
count=0
for i in range(0,len(a)):
    if (a[i]<='9' and a[i]>'0' )or (a[i]>='A' and a[i]<='F'):
        count=count+1 
        
if count==len(a):
    print("yes")
else:
    print("no")
