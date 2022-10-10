s = 'XOXOXOXOXOOX'
n = len(s)
def ktdx(a,b):
	for i in range(a):
		for j in range(b):
			print(a,b)
			if s[j] == s[j+b] == 'X':
				return True
	return False
for a in range(1,n+1):
	if n % a == 0:
		b = 12 //a
		if ktdx(a,b):
			print(a,b)
