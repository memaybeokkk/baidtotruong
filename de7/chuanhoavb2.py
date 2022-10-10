a = ['ab3c1x2y3z','23sa','cb1','1cd7h2d']
b = []
c = []
for i in range(len(a)):
	d = 0
	for j in range(len(a[i])):
		if '0' <= a[i][j] <= '9':
			d = d + 1
	c.append(d)
for i in range(len(c)):
	for j in range(i+1,len(c)):
		if c[j] < c[i]:
			temp = c[i]
			c[i] = c[j]
			c[j] = temp 
			temp1 = a[i]
			a[i] = a[j]
			a[j] = temp1
print(a,c)