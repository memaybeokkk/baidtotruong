f = open('tamgiacso.INP','r')
n = int(f.readline())
d = 1
c = [0] * (n+1)
F = [0] * (n+1)
for i in range(n+1):
	c[i] = [0] * (n+1)
	F[i] = [0] * (n+1)
for k in f:
	a = [0] + [int(i) for i in k.split()]
	for j in range(1,len(a)):
		c[d][j] = a[j]
	d+=1
F[1][1] = c[1][1]
for i in range(2,n+1):
	F[i][1] = F[i-1][1] + c[i][1] 
for i in range(2,n+1):
	for j in range(2,n+1):
		if F[i-1][j] > F[i-1][j-1]:
			F[i][j] = F[i-1][j] + c[i][j]
		else:
			F[i][j] = F[i-1][j-1] + c[i][j]
max = 0
for i in range(1,n+1):
	if F[n][i] > max:
		max = F[n][i]
		cs = i
print(i,max)