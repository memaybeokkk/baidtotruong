from math import sqrt
a = [True] * 100000
a[0] = a[1] = False
for i in range(2,int(sqrt(100000))):
	if a[i] == True:
		for j in range(2,100000//i):
			a[i*j] = False
d = [0] * 1000
n = 300
i = 2
while n != 1:
	if a[i] == True:
		while n % i == 0:
			d[i] = d[i] + 1
			n = n / i
		if d[i] == 1:
			print(str(i),end='')
		else:
			print(str(i)+'^'+str(d[i]),end='')
		if n == 1:
			break
		print('.',end='')
	i+=1
