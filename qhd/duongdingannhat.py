f = open('duongdingannhat.INP','r')
a = [int(i) for i in f.readline().split()]
n = a[0]
m = a[1]
s = a[2]
F = a[3]
c = [0] * (n+1)
max = 10000
for i in range(n+1):
	c[i] = [0] * (n+1)
for i in range(n+1):
	for j in range(n+1):
		c[i][j] = max
for k in f:
	b = [int(i) for i in k.split()]
	u = b[0]
	v = b[1]
	c[u][v] = b[2]
for i in range(n+1):
	for j in range(n+1):
		print(c[i][j],' ',end=' ')
	print()
f.close()
d = [0] * (n+1)
for i in range(n+1):
	d[i] = max 
d[s] = 0
Fr = [0] * (n+1)
Truoc = [0] * (n+1)
while u!=F and u !=0:
	u = 0 
	min = max
	for v in range(1,n+1):
		if d[v] < min and Fr[v] == 0:
			min=d[v]
			u = v
	Fr[u] = 1
	if u!= F and u !=0:
		for v in range(1,n+1):
			if d[v] > d[u] + c[u][v] and Fr[v] == 0:
				d[v] = d[u] + c[u][v]
				Truoc[v] = u
x=''
x=x+'='+str(F)

