def permutations(a):
    lst1=[]
    if len(a)==0:
        return []
    if len(a)==1:
        return [a] 
        j=1
    for i in range(j,len(a)):
        m=a[i]
        remlst=a[::i]+a[i+1]
        for p in permutations(remlst):
            lst1.append([m]+p)
    return lst1
        
a=list(input())
for p in permutations(a):
    print(lst1)    

