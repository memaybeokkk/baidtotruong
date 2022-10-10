from math import *
n = int(input())
snt = [True] * 1000000
snt[0] = snt[1] = False
for i in range(2,int(sqrt(1000000))):
	if snt[i] == True:
		for j in range(2,1000000//i):
			snt[i*j] = False
lst = []
for i in range(2,n):
	if n % i == 0:
		lst.append(i)
s = []
for i in lst:
	while n%i==0:
		n = n / i
		s.append(i)
		if n <= 1:
			break
s = set(s)
s2 = sum(s)
print(s,s2)


