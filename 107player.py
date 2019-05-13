str1=input().split()
str2=input().split()
for i in range(0,len(str1)):
    for j in range(0,len(str2)):
        if str2[j]==str1[i]:
            print(i+1)
