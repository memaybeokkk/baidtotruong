for i in range(1000,10000):
	for j in range(0,4):
		s = i.pop(j)
		if s == i/9:
			print(i)
			break

