from math import sqrt
a = [True] * 1000000
s = ''
dem = 0
n = 5
k = 4
a[0] = a[1] = False
for i in range(2,int(sqrt(1000000))):
	if a[i] == True:
		for j in range(2,1000000//i):
			a[i*j] = False
		s = s + str(i)
		dem+=1
		if dem == n:
			break
d = -1
nk = len(s) - k
while k != 0 or (d+1) != nk:
	d = d + 1
	max = s[d]
	vt = d
	for i in range(d+1,d+k+1):
		if s[i] > max:
			max = s[i]
			vt = i
	if d == 0:
		s = s[vt:]
	else:
		s = s[:d] + s[vt:]
	k = k - vt + d
	if k == 0 or d+1 == nk:
		break
if k > 0:
	s = s[:d+1]
print(s)