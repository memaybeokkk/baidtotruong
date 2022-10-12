a = [1,1,1,1,1,1,1,1,1,0]
a = [1] + a + [1]
min = 99999999999999
d = 0
i = 1
while i < len(a):
	if a[i] == 0:
		d = 0
		while a[i] == 0:
			d+=1
			i+=1
		if d < min:
			min = d
	i+=1
print(min)
