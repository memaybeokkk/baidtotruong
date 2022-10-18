n = 14
a = [12,-34,14,11,9,-8,15,11,-7,-56,17,16,19]
a = [0] + a
L = [0] * n
T = [0] * n
T[0] = a[0]
tmax = -9999999999999
dmax = 0
csd = []
csc = []
for i in range(1,n):
	T[i] = T[i-1] + a[i]
for i in range(1,n):
	for j in range(i,n):
		if T[j] - T[i-1] > tmax:
			tmax = T[j] - T[i-1]
			csd = [i]
			csc = [j]
		elif T[j] - T[i-1] == tmax:
			csd.append(i)
			csc.append(j)
print(tmax,len(csd))
for i in range(len(csd)):
	for j in range(csd[i],csc[i]+1):
		print(a[j])
	print('done')