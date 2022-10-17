n = 6
s = 98
a = [1,2,5,10,50,100]
l = len(a)
L = [0] * (s+1)
KQ = [0] * (s+1)
b = [0] * (s+1)
for i in range(1,s+1):
	for j in range(n):
		if a[j] <= i:
			if L[i] == 0 or L[i-a[j]] < L[i]:
				L[i] = L[i-a[j]] + 1
				KQ[i] = j
print(L[s])
while s>0:
	b[KQ[s]] = b[KQ[s]] + 1
	s = s- a[KQ[s]]
for i in range(n):
	if b[i] >= 0:
		print(i,'',b[i])