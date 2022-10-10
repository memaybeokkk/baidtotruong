n = [3,8,5,1,2,12,9]
from math import sqrt
a = [True] * (1000000)
a[0] = a[1] = False
d = 0
for i in range(2,int(sqrt(1000000))):
	if a[i] == True:
		for j in range(2,1000000//i):
			a[i*j] = False
i = 2
print(a[0:10])
mini = min(a)
maxi = max(a)
while True:
	if i not in n and a[i] == True:
		if i < mini or i > maxi:
			print(i)
			break
	i+=1
