def ae(a,b):
	kt = True
	for i in a:
		if b.count(i) == 0:
			kt = False
			return kt
	for i in b:
		if a.count(i) == 0:
			kt = False
			return kt
	return kt

print(ae)