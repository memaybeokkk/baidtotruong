a = [5,2,3,4,9,10,5,6,7,8]
a = [-99999] + a + [99999]
n = len(a)
L = [0] * (n)
L[n-1] = 1
T = [0] * (n)
for i in range(n-2,-1,-1):
	jmax = n - 1
	for j in range(i+1,n):
		if a[i] < a[j] and L[j] > L[jmax]:
			jmax = j
	L[i] = L[jmax] + 1
	T[i] = jmax

print(L,T)
i = T[0]
while i != n-1:
	print(a[i],end='')
	i = T[i]
