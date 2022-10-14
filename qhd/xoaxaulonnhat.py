p = 3; k =11
a = [3,4,2]
s = [123,0,45]
t = ''
for i in range(p):
	for j in range(a[i]):
		t+=str(s[i])
print(t)
d = 0
while k != 0 and d<len(t)-k :
	max = t[d]
	vt = d
	for i in range(d,d+k+1):
		if int(t[i]) > int(max):
			max = t[i]
			vt = i
	t = t[:d] + t[vt:]
	k = k - vt + d
	d+= 1
	print(d,t)
print(k,t,d)
if k > 0:
	t = t[:d]
print(t) 