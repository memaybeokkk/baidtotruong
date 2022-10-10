with open('ZERO.INP','r') as tep1:
	n = int(tep1.readline())
	s = tep1.readline()
a = [int(x) for x in s.split()]
dmax = 0
f = [0] * n
f[0] = a[0]
for i in range(1,n):
	f[i] = f[i-1] + a[i]
for i in range(1,n-1):
	for j in range(i+1,n):
		if f[j] - f[i-1] == 0:
			if j - i + 1 > dmax:
				dmax = j - i +1

with open('ZERO.OUT','w') as tep2:
	tep2.write(str(dmax))