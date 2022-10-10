s1 = 'a19012304'
s2 = 'a034012'
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
vt = []
max = L[n-1][m-1]
for i in range(m-1,1,-1):
	if L[n-1][i] == max:
		vt.append(i)
dmax = 0

for k in range(len(vt)):
	i = n - 1
	j = vt[k]
	c = ''
	while i != 0 and j != 0:
		if s2[i] == s1[j]:
			c = s2[i] + c
			i = i - 1
			j = j - 1
		elif L[i][j] == L[i-1][j]:
			i = i - 1
		else:
			j = j - 1
	print(c)
	if dmax < int(c):
		dmax = int(c)

print(dmax)