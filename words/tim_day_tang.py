tep1 = open('Daycontang.inp','r')
tep2 = open('Daycontang.out','w')
s1 = tep1.readline()
s2 = tep1.readline()
a = [int(x) for x in s2.split()]
f = [0] * int(s1)
f[0] = 1
dmax = 0
cs = []
for i in range(0,int(s1) -1):
	if a[i+1] > a[i]:
		f[i+1] = f[i] + 1
	else:
		f[i+1] = 1
	if f[i+1] > dmax:
		dmax = f[i+1]
		cs = [i+1]
	elif f[i+1] == dmax:
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