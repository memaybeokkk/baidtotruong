a = [1,7,2,6,10,6,1,5,9]
n = len(a)
f = [0] * n 
f[0] = 1
d = 4
cs = []
dmax = 0
for i in range(0,n-1):
	if a[i+1] - a[i] == d:
		f[i+1] = f[i] + 1
	else:
		f[i+1] = 1
	if f[i+1] > dmax:
		dmax = f[i+1]
		cs = [i+1]
	elif f[i+1] == dmax:
		cs.append(i+1)
print(dmax,len(cs))
for i in range(len(cs)):
	for j in range(cs[i] - dmax + 1, cs[i] + 1):
		print(a[j],end=' ')
	print()
