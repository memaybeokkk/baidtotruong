s1 = 'adsajjasgbbsbadasdjda'
s2 = s1[::-1]
s1 = '0' + s1
s2 = '0' + s2
m = len(s1)
n = len(s2)
L = [0] * n
for i in range(n):
	L[i] = [0] * m
for i in range(n):
	for j in range(m):
		if s2[i] == s1[j]:
			L[i][j] = L[i-1][j-1] + 1
		else:
			L[i][j] = max(L[i][j-1],L[i-1][j])
i = n - 1
j = m - 1
a = []
while i != 0 and j != 0:
	if s2[i] == s1[j]:
		a.append(s2[i])
		i = i - 1
		j = j - 1
	elif L[i][j] == L[i-1][j]:
		i = i - 1
	else:
		j = j - 1
a.sort()
a = ''.join(a).lstrip('0')
print(a)
