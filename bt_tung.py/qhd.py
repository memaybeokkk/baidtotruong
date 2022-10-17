a = [4,6,1,-1,9]
n = len(a)
s = 5
L = [0] * 7
L[0] = 1
tmax = 0
for i in range(n):
	max = tmax
	for st in range(tmax,-1,-1):
		if st + a[i] > s:
			continue
		if L[st] != 0 and L[st+a[i]] == 0:
			L[st+a[i]] = i
			if st + a[i] == s:
				break
			if st + a[i] > max:
				max = st + a[i]
	tmax = max		
print(L)	
while s > 0:
	i = L[s]
	print(a[i],end=' ')
	s = s - a[i]
	