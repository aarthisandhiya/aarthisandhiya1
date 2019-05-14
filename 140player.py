a=input()
b=len(a)
count=0
for i in range(0,b):
    if a[i]=='a' or a[i]=='b':
        count=count+1 
if count==b:
    print("yes")
else:
    print("no")
