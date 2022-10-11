from collections import Counter
a = 'Gg&^56@gd89d001aA'
d = list(a)
dic = Counter(a)
b = list(dic.values())
c = list(dic.keys())
max = 0
for i in range(len(b)):
	if b[i] > max:
		max = b[i]
		dmax = i
print(dic)
print(c[dmax],b[dmax])
