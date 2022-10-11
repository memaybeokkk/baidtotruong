n = 5
m = 3
a = [0,1,3,2,5]
T = [0] * n
dmax = 0
csd = []
csc = []
for i in range(1,n):
	T[i] = T[i-1] + a[i]
print(T)
for i in range(1,n):
	for j in range(i,n):
		if (T[j] - T[i-1])%m == 0:
			csd.append(i)
			csc.append(j)
print(len(csd))
for i in range(len(csd)):
	for j in range(csd[i],csc[i]+1):
		print(a[j],end=' ')
	print()







