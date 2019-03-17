a=int(input())
b=[int(a) for a in input().split()]
mini=b[0]
maxi=b[0]
c=0
for i in b:
    if i>maxi:
        maxi=i 
for i in b:
    if i<mini:
        mini=i 
c=maxi-mini
print(c)
        
