n = int(input())
T = [0] * (n+1)
T[0] = 0
csd	= []
csc = []
for i in range(1,n):
	T[i] = T[i-1] + i
for i in range(n):
	for j in range(i,n):
		if T[j] - T[i-1] == n:
			print(T[j],T[i-1])
			csd.append(i)
			csc.append(j)
for i in range(len(csd)):
	for j in range(csd[i], csc[i]+1):

		print(j,sep='+',end=' ')
	print()
