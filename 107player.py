str11=input().split()
str22=input().split()
for i in range(0,len(str11)):
    for j in range(0,len(str22)):
        if str22[j]==str11[i]:
            print(i+1)
