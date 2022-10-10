a = [1,5,3,0,2,1,4,3,6,8]
d = 2
n = len(a)
L = [0] * (n)
L[n-1] = 1
dmax = 0
for i in range(1,n):
	jmax = 0
	for j in range(i-1,-1,-1):
		if a[i] - a[j] == d and L[j] > L[jmax]:
			jmax = j
	L[i] = L[jmax] + 1
	if L[i] > dmax:
		dmax = L[i]

print(dmax)