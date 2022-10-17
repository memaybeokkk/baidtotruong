s = 'OXXXOXOOXOOX'
def ktx(a,b):
	for j in range(b):
		kt = True
		for i in range(1,a+1):
			if s[(i-1) * b + j] != 'X':
				kt = False
				break
		if kt == True:
			return kt
	return kt 
d = 0
l = []
for a in range(1,13):
	if 12% a == 0:
		b = 12//a 
		if ktx(a,b):
			d+=1
			l.append(str(a) + 'x' + str(b))
print(d,end=' ')
for i in l:
	print(i,end=' ')