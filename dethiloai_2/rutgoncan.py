from math import sqrt
f2 = open('Bai4.out','w')
with open('Bai4.inp','r') as f1:
	T = int(f1.readline())
	lst = []
	for i in range(T):
		lst.append(int(f1.readline()))
def rgcan(n):
	a = int(sqrt(n))
	b = n / a**2
	if int(b) != b:
		a = 1
		b = n
	b = int(b)
	return str(a)+ ' ' + str(b)
for i in lst:
	f2.write(rgcan(i))
	f2.write('\n')


















f2.close()