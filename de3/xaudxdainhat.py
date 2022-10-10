a = '1121034515438'
dmax = 0
def xaudx(i,j):
	s = a[i:j+1]
	for x in range(len(s)//2+1):
		if s[x] != s[len(s)-x-1]:
			return False
	return True
for i in range(len(a)-1):
	for j in range(i,len(a)):
			if xaudx(i,j):
				if len(a[i:j+1]) > dmax:
					dmax = len(a[i:j+1])
					vtd = i
					vtc = j + 1

print(dmax,a[vtd:vtc])
