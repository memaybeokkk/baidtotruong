a = [8,7,6,5,3,9,7,6]
print(set(a))
for i in a:
	if a.count(i)== 1:
		print(i)