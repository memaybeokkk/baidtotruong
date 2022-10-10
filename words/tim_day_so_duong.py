tep1 = open('Dayconduong.inp','r')
tep2 = open('Dayconduong.out', 'w')
s1 = tep1.readline()
s2 = tep1.readline()
a = [int(x) for x in s2.split()]
f = [0] * int(s1)
if a[0] > 0:
	f[0] = 1
else:
	f[0] = 0
dmax = 0
for i in range(1,int(s1)):
	if a[i] > 0:
		f[i] = f[i-1] + 1
	else:
		f[i] = 0 
	if f[i] > dmax:
		dmax = f[i]
		cs = [i]
	elif f[i] == dmax: 
		cs.append(i)		
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