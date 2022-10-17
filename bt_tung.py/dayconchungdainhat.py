f2 = open('Daycon.OUT','w')
with open('Daycon.INP','r') as f1:
	n = int(f1.readline())
	a = [int(i) for i in f1.readline().split()]
	a = [0] + a
	m = int(f1.readline())
	b = [int(i) for i in f1.readline().split()]
	b = [0] + b
n1 = len(a)
n2 = len(b)
L = [0] * n2
for i in range(n2):
	L[i] = [0] * n1
for i in range(1,n2):
	for j in range(1,n1):
		if b[i] == a[j]:
			L[i][j] = L[i-1][j-1] + 1
		else:
			L[i][j] = max(L[i-1][j],L[i][j-1])
print(L[i][j])
i = n2 - 1
j = n1 - 1
c = []
while i != 0 and j != 0:
	if b[i] == a[j]:
		c.append(b[i])
		i = i - 1
		j = j - 1
	elif L[i][j] == L[i-1][j]:
		i = i - 1
	else:
		j=j-1
c = c[::-1]
print(c)
for i in c:
	print(a.index(i),end=' ')
print()
for i in c:
	print(b.index(i),end=' ')
f2.close()
