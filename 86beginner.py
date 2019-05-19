word=input()
c=0
for char in word:
    if word.count(char) > 1:
        c=c+1 
if c>0:
    print("yes")
else:
    print("no")
