n = 4
m = 7
v = [0,5,3,2,5]
w = [0,1,2,6,7]
L = [0] * (n+1)
for i in range(n+1):
	L[i] = [0] * (m+1)
for i in range(n+1):
	print(L[i])
print()
for i in range(1,n+1):
	for j in range(1,m+1):
		L[i][j] = L[i-1][j]
		if w[i] <= j and L[i][j] < v[i]+L[i-1][j-w[i]]:
			L[i][j] = v[i]+L[i-1][j-w[i]]		
for i in range(n+1):
	print(L[i])
value = 0
while n != 0:
	if L[n][m] != L[n-1][m]:
		print(v[n],w[n],m,sep=' ')
		value = value + v[n]

		m = m - w[n]
	n = n - 1
print(value) 