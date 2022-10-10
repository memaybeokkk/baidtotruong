s = input()
i = 0
a = []
dmax = 0
tmax = ''
while i <= len(s)-1:
	t = ''
	while i<= len(s)-1 and ('a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z'):
		t+= s[i]
		i+= 1
	if t != '':
		a.append(t)
		if len(t) > dmax:
			dmax = len(t)
			tmax = t
	i+= 1

print(a)
print(dmax,tmax)