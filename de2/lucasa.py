def lucasa(a,b):
	b = str(b)
	if a**2 == int(b):
		d1 = len(str(a))
		if int(b[-d1:]) == a:
			return True
print(lucasa(1,1))