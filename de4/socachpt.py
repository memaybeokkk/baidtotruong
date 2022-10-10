n = int(input())
T = [0] * n
csd = []
csc = []
for i in range(1,n):
	T[i] = T[i-1] + i
for i in range(n):
	for j in range(i,n):
		if T[j] - T[i-1] == n:
			csd.append(i)
			csc.append(j)
print(str(n)+'='+str(n),end='\n')
for i in range(len(csd)):
	print(str(n)+' = ',end=' ')
	for j in range(csd[i],csc[i]+1):
		print(str(j)+'+',end='')
	print()