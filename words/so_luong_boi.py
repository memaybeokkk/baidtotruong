d = []
with open('MULT.INP','r') as tep1:
	a = int(tep1.readline())
	dem = 0
	for i in range(a):
		s = tep1.readline()
		b = s.split()
		n = int(b[0])
		x = int(b[1])
		for j in range(1,x//2 + 1):
			if j * n <= x:
				dem+=1
		d.append(dem)
		dem = 0
with open('MULT.OUT','w') as tep2:
	for i in range(a):
		tep2.write(str(d[i]) + '\n')


