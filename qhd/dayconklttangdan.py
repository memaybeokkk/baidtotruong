n = 10
a = [5,1,6,4,5,2,1,7]
a = [-999999999] + a + [999999999]
L = [0] * n
T = [0] * n
L[n-1] = 1
for i in range(n-2,-1,-1):
	jmax = i
	for j in range(i+1,n):
		if a[j] > a[i] and L[j] > L[jmax]:
			jmax = j 
	L[i] = L[jmax] + 1
	T[i] = jmax 
print(L,T)
i = T[0]
while i != n-1:
	print(str(a[i])+' ')
	i = T[i]

