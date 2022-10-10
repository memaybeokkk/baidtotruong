tep1 = open('Dayconcsc.inp','r')
tep2 = open('Dayconcsc.out','w')
n = tep1.readline()
ds = n.split()
n1 = int(ds[0])
d = int(ds[1])
ds2 = tep1.readline()
a = [int(x) for x in ds2.split()]
f1 = [0] * n1
f1[0] = 1
dmax = 0 
cs = []
for i in range(0,n1 - 1):
	if a[i+1] - a[i] == d:
		f1[i+1] = f1[i] + 1
	else:
		f1[i+1] = 1
	if f1[i+1] > dmax:
		dmax = f1[i+1]
		cs = [i + 1]
	elif f1[i+1] == dmax:
		cs.append(i+1)
if dmax == 1:
	tep2.write('0')
else:
	tep2.write(str(dmax) + ' ' +str(len(cs)) + '\n')
	for i in range(len(cs)):
		for j in range(cs[i] - dmax + 1, cs[i] + 1):
			tep2.write(str(a[j]) + ' ')
		tep2.write('\n')
tep1.close()
tep2.close()