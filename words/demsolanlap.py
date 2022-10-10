s = input()
i = 0
a = ''
while i < len(s) -1:
	d = 1
	while s[i] == s[i+1] and i < len(s)-1:
		d+= 1
		i+= 1
		if i == len(s)-1:
		    break
	
	a = a + str(d) + s[i]
	i+= 1
if s[-1] != s[-2]:
	a = a + str(1) + s[-1]
print(a)