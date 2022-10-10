s1 = '0abcdeb'
s2 = '0bcefa'
m = len(s1)
n = len(s2)
L = [0] * n
for i in range(n):
	L[i] = [0] * m 
for i in range(1,n):
	for j in range(1,m):
		if s2[i] == s1[j]:
			L[i][j] = L[i-1][j-1] + 1
		else:
			L[i][j] = max(L[i][j-1],L[i-1][j])
for i in range(n):
	for j in range(m):
		print(L[i][j],end=' ')
	print()
i = n - 1
j = m - 1
c = []
print(n,' ',m)
print(s2[i],' ',s1[j])
while i != 0 and j != 0:
	if s2[i] == s1[j]:
		print(s2[i])
		c.append(s2[i])
		i = i - 1
		j = j - 1
	elif L[i][j] == L[i-1][j]:
		i = i - 1
	else:
		j=j-1
print(c)