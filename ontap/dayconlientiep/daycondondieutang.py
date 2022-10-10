n = 12
a = [5,2,3,8,9,10,8,6,7,11,20,33]
f = [0] * n
f[0] = 1
dmax = 0
cs = []
for i in range(n-1):
	if a[i+1] > a[i]:
		f[i+1] = f[i] + 1
	else:
		f[i+1] = 1
	if f[i+1] >dmax :
		dmax = f[i+1]
		cs = [i+1]
	elif f[i+1] == dmax:
		cs.append(i+1)
print(dmax,len(cs))
for i in range(len(cs)):
	for j in range(cs[i] - dmax +1,cs[i]+1):
		print(a[j],end=' ')
	print()
