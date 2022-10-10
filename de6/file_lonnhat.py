n, Q = [int(i) for i in input().split()]
w = []
u = []
v = []
for i in range(n):
	w.append(int(input()))
for i in range(Q):
	ui, vi = [int(j) for j in input().split()]
	u.append(ui-1)
	v.append(vi-1)
dmax = []
for i in range(Q):
	max = 0
	for j in range(u[i],v[i]+1):
		if w[j] > max:
			max = w[j]
	dmax.append(max)
for i in dmax:
	print(i)
