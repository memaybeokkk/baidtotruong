n = 7
a = [3,2,5,1,8,6,3]
L = [0] * (s+1)
Tmax = 0
L[0] = 1
for i in range(n):
	for st in range(Tmax,-1,-1):
		if st + a[i] > s:
			continue
		if L[st] != 0 and L[st+a[i]] ==0:
			L[st+a[i]] = i
			if st + a[i] == s:
				break
			if st + a[i] > Tmax:
				Tmax = st + a[i]
i = L[s]
while s > 0:
	if i >= 0:
		print(a[i],' ',end=' ')
		s = s - a[i]
		i = L[s]
	