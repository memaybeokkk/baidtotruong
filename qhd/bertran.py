from math import sqrt
a = [True] * 10000000
a[0] = a[1] = False
d = 0
for i in range(2,int(sqrt(10000000))):
	if a[i] == True:
		for j in range(2,10000000//i):
			a[i*j] = False
for i in range(n,n*2):
	if a[i] == True:
		d+=1
