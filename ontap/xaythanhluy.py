a = 'daica'
b = []
for i in range(len(a)):
	for j in range(i,len(a)):
		if a[i:j+1] not in b:
			b.append(a[i:j+1])
print(b,len(b))