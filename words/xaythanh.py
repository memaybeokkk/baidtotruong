s = 'ABAB'
b = []
for i in range(len(s)):
	a = ''
	for j in range(i,len(s)):
		a = a + s[j]
		if a not in b:
			b.append(a)
print(len(b))