from math import sqrt
n = 20
a = []
i = 2
d = [0] * 20
p = 1
while n != 1:
	while n % i == 0:
		d[i] = d[i] + 1
		n = n // i
	if d[i] >= 1:		
		a.append(i)
	i+=1
for i in a:
	p = p*i
print(p)

