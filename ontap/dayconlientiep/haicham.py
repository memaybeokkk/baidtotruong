from collections import Counter
a = [1,2,4,6,2,2,4,4,4,6,3]
dic = Counter(a)
c = list(dic.keys())
b = list(dic.values())
d = min(dic,key=dic.get)
max = 0
print(d)
for i in range(len(b)):
	if b[i] > max:
		max = b[i]
		dmax = i
print(dic)
print(c[dmax],b[dmax])
