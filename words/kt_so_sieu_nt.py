from math import *
b = [7,235,525,2333,2334]
a = [True] * 100000
a[0] = a[1] = False
for i in range(2,int(sqrt(100000))+1):
	if a[i] == True:
		for j in range(2,100000//i):
			a[i*j] = False

def ssnt(x):
	global a
	kt = True
	while x > 1:
		if not a[x]:
			kt = False
			break
		x = x // 10 
	return kt 

for i in b:
	print(ssnt(i))