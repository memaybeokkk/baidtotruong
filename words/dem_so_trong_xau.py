a,b = input().split()
d =[0] * 10
for i in range(a,b+1):
	s1 = str(i)
	for j in s1:
		d[int(j)] = d[int(j)] + 1
for i in range(0,10):
	print(d[i], end='')