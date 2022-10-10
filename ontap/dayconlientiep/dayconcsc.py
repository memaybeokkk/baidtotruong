n = 9 
d = 4
a = [1,7,2,6,10,6,1,5,9]
f = [0] * n
f[1] = 1
dmax = 0
cs = []
for i in range(n-1):
	if a[i+1] - a[i] == d:
		f[i+1] = f[i] + 1
	else:
		f[i+1] = 1
	if f[i+1] > dmax:
		dmax = f[i+1]
		cs = [i+1]
	elif f[i+1] == dmax:
		cs.append(i+1)
if dmax == 1:
	print(0)
else:
	print(dmax,len(cs))
	for i in range(len(cs)):
		for j in range(cs[i]-dmax+1,cs[i]+1):
			print(a[j],end='')
		print()