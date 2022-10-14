p = 3; k = 3
a = [3,4,2]
s = [123,0,45]
t = ''
for i in range(p):
	for j in range(a[i]):
		t+=str(s[i])
print(t,len(t))
d = 0
while k !=0 and d < len(t) - k:
	min = t[d]
	vt = d
	for i in range(d+1,d+k+1):
		if int(t[i]) < int(min):
			min = t[i]
			vt = i
	t = t[:d] + t[vt:]
	k = k - vt + d
	d = d + 1
print(t,d)
