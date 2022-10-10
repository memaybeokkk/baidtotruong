f2 = open('DACSAN.OUT','w')
with open('DACSAN.INP','r') as f1:
	a, b, c = [int(i) for i in f1.readline().split()]
	dem = 0
	print(a,b,c)
	while a!= 0 and b!= 0 and c != 0:
			dem = dem + 1
			a = a - 1
			b = b - 1
			c = c - 1
	if a == 0:
		if b >= 3:
			dem = dem + b//3
			b = b - b//3
		if c >= 3:
			dem = dem + c//3
			c = c - c//3
	if b == 0:
		if a >= 3:
			dem = dem + a//3
			a-=a//3
		if c >= 3:
			dem = dem + c//3
			c = c - c//3
	if c == 0:
		if b >= 3:
			dem = dem + b//3
			b = b - b//3
		if a >= 3:
			dem = dem + a//3
			a = a - a//3


print(dem)
f2.close()

