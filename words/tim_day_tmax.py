with open('Tonglt.inp','r') as tep1:
	s1 = int(tep1.readline())+1
	s2 = tep1.readline()
a = [0] + [int(x) for x in s2.split()]
tep2 = open('Tonglt.out', 'w')
T = [0] * s1
T[0] = a[0]
tmax = -999999999999
csd = []
csc = []
out = ''
for i in range(1,s1):
	T[i] = T[i-1] + a[i]
print(T)
for i in range(1,s1):
	for j in range(i, s1):
		if T[j] - T[i-1] > tmax:
			tmax = T[j] - T[i-1]
			csd = [i]
			csc = [j]
		elif T[j] - T[i-1] == tmax:
			csd.append(i)
			csc.append(j)
print(tmax,csd,csc)
print(a,T,sep='\n')
if tmax == 0:
	tep2.write('0')
else:
	tep2.write(str(tmax) + ' ' +str(len(csd)) + '\n')
	for i in range(len(csd)):
		for j in range(csd[i],csc[i] + 1):
			out = out + str(a[j]) + ' '
		tep2.write(out.rstrip(' '))		
		tep2.write('\n')
		out = ''
tep2.close()