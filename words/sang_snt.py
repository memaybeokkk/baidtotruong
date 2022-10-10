from math import *
a = [True] * 10
a[0] = a[1] = False
for i in range(2,int(sqrt(10))):
	if a[i] == True:
		for j in range(2,10//i):
			a[i*j] = False
print(a)
