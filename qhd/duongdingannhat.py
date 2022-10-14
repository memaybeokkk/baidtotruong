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
'''
f2=open('ggmap.out','w')
f1=open('ggmap.inp','r')
a=[int(x) for x in f1.readline().split()]
n=a[0]+1;m=a[1];s=a[2];f=5
c=[0]*n 
max=999999
for i in range(n):
	c[i]=[max]*n
for i in f1:
	a=[int(x) for x in i.split()]
	c[a[0]][a[1]]=a[2]
d=[max]*n 
fr=[0]*n 
truoc=[0]*n 
d[s]=0  
u=s 
while u!=f and u!=0:
	min=max 
	for v in range(1,n):
		if d[v]<min and fr[v]==0:
			min=d[v]
			u=v 
	fr[u]=1 
	for v in range(1,n):
		if d[v]>d[u]+c[u][v] and fr[v]==0:
			print(v,d[u]+c[u][v])
			d[v]=d[u]+c[u][v]
			truoc[v]=u 

di=[u]
while truoc[u]!=0:
	di.append(truoc[u])
	u=truoc[u]
print(di[::-1])
