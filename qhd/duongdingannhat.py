'''
f = open('duongdingannhat.INP','r')
a = [int(i) for i in f.readline().split()]
n = a[0]
m = a[1]
s = a[2]
F = a[3]
c = [0] * (n+1)
max = 10000
for i in range(n+1):
	c[i] = [max] * (n+1)

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

while truoc[u] != 0:
	print(truoc[u])
	u=truoc[u]
'''
f2=open('ggmap.out','w')
f1=open('ggmap.inp','r')
n=int(f1.readline())+1
max=999999
c=[[max]*n]

for i in f1:
	c.append([max]+[int(x) for x in i.split()])
import itertools
def SUM(i):
	return c[i[0]][i[1]]+c[i[1]][i[2]]+c[i[2]][i[3]]+c[i[3]][i[4]]+c[i[4]][i[0]]
d=list(itertools.permutations([2,3,4,5]))
b=[]
for i in d:
	b.append([1]+list(i))
dmin=max
min='a'
for i in b:
	if SUM(i)<dmin:
		dmin=SUM(i)
		min=' '.join(str(x) for x in i)
		min+= ' 1'
print(dmin,min)
