from math import *
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
m = int(input())
s1 = []
s2 = []
i = 1
j = 1
while s1 == []:
	if ssnt(m-i):
		s1.append(m-i)
		break
	else:
		i+=1
while s2 == []:
	if ssnt(m+j):
		s2.append(m+j)
		break
	else:
		j+=1
if abs(m-s1[0]) < abs(m-s2[0]):
	print(s1[0])
elif abs(m-s1[0]) > abs(m-s2[0]):
	print(s2[0])
else:
	print(s1[0],s2[0],sep='\n') 