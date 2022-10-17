a = [4,6,1,-1,9]
a = [0] + a
n = len(a)
M = 5 
L = [0] * (n+1)
L[0] = 1
tmax = 0
for i in range(1,n):
	max = tmax
	for st in range(tmax,-1,-1):
		if st + a[i] > M:
			continue
		if L[st] != 0 and L[st+a[i]] == 0:
			L[st+a[i]] = i
			if st + a[i] == M:
				break
			if st + a[i] > max:
				max = st + a[i]
	tmax = max
print(L)			
while M > 0:
	i = L[M]
	print(a[i],end=' ')
	M = M - a[i]
	
