s = 'Hoc tin rat thu vi'
s = s.split()
max = 0
for i in s:
	if len(i) > max:
		max = len(i)
		xau = i
print(xau)