a = [int(i) for i in input().split()]
a = [-99999] + a + [99999]
n = len(a)
L = [0] * (n+1)
L[n-1] = 1
T = [0] * (n+1)
for i in range(n-2,-1,-1):
	jmax = n - 1
	for j in range(i+1,n):
		if a[i] < a[j] and L[j] > L[jmax]:
			jmax = j
	L[i] = L[jmax] + 1
	T[i] = jmax
i = T[0]
while i != n-1:
	print(a[i],end=' ')
	i = T[i]
