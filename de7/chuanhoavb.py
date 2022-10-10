a = ['ab3c1x2y3z','23sa','cb1','1cd7h2d']
b = []
c = []
for i in range(len(a)):
	d = 0
	for j in range(len(a[i])):
		if '0' <= a[i][j] <= '9':
			d = d + 1
	b.append(a[i])
	c.append(d)
d = [x for _,x in sorted(zip(c,b),reverse=True)]
print(d)
