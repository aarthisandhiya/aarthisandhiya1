v=int(input())
string=[str(v) for v in input()]
vowel='aeiouAEIOU'
newstr=''
for i in string:
	if i not in vowel:
		newstr+=i
c=newstr[::-1]
print(c)
