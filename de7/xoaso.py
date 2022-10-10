s = '124512hoctin8126123'
t = ''
for i in s:
	if '0' <= i <= '9':
		t+=i
d = 0
k = len(t) - 3
while len(t) != 3:
	max = 0
	vt = d
	for i in range(d+1,d+k+1):
		if int(t[i]) > max:
			max = int(t[i])
			vt = i
	t = t[:d] + t[vt:]
	k = k - vt + d
	d = d + 1
print(t)