n = '202'
a = []
for i in range(len(n)):
	for j in range(1,len(n)):
		s = n[i:j+1].lstrip('0')
		if s != '' and s not in a:
			a.append(s)
T = sum(a)
print(T)
