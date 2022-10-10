s = 'aaabbbaaabbbaaa'
n = len(s)
kt = True
for i in range(n):
	if s[i] != s[n-i-1]:
		kt = False
		break
if kt == True:
	print('co')
else:
	print('khong')