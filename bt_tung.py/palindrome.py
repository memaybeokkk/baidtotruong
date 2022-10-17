s = 'array'
for i in range(len(s)//2+1):
	s = s[-1] + s[:len(s)-1]
	if s[::-1] == s:
		print('YES')
		break
if s[::-1] != s:
	print('NO')
