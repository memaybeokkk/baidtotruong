f2 = open('BT1.out','w')
with open('BT1.inp','r') as f1:
	n = f1.readline()
	for i in f1:
		c = [int(j) for j in i.split()]
		d =[0] * 10
		if c[0] == c[1] == 0:
			break
		for i in range(c[0],c[1]+1):
			s1 = str(i)
			for j in s1:
				d[int(j)] = d[int(j)] + 1
		for i in range(0,10):
			f2.write(str(d[i])+' ')
		f2.write('\n')
f2.close()