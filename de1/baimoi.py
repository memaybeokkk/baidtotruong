s = '12935924'
k = 5
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
	print(max,vt)
	if d == 0:
		s = s[vt:]
	else:
		s = s[:d] + s[vt:]
	k = k - vt + d
	print(s,k)
	if k == 0 or d+1 == nk:
		break
if k > 0:
	s = s[:d+1]
print(s)