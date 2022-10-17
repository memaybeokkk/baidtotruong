a = []
s = 'ab43bcd0gh'
j = 0
print(s)
while j < len(s):
	x = ''
	while '0' <= s[j] <= '9' and j < len(s):
		x+=s[j]
		j+=1
	if x != '':
			if x == '0':
					a.append(x)
			else:
					a.append(x.lstrip('0'))
	j+=1
print(a)