n = 6
s = 98 
a = [1,2,5,10,50,100]
L = [0] * (s+1)
kq = [0] * (s+1)
b = [0] * (s+1)
for i in range(1,s+1):
	for j in range(n):
		if a[j] <= i:
			if L[i] == 0 or L[i-a[j]] + 1 < L[i]:
				L[i] = L[i-a[j]] + 1
				kq[i] = j
print(L[s])
while s>0:
	b[kq[s]] = b[kq[s]] + 1
	s = s - a[kq[s]]
for i in range(n):
	if b[i] >= 0:
		print(i,'',b[i])