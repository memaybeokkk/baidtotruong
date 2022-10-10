from math import sqrt
a = [True] * (1000)
a[0] = a[1] = False
d = 0
for i in range(2,int(sqrt(1000))):
	if a[i] == True:
		for j in range(2,1000//i):
			a[i*j] = False
n = 9
t = ''
i = 2
while n != 0:
	if a[i] == True and n % i == 0:
		while n % i == 0:
			n= n / i
			t+=str(i)

	i+=1
print(t)