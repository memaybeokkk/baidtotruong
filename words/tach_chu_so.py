s = 'adwuh235kda24k'
chu = ''
so = ''

for i in s:
	if 'a' <= i <= 'z':
		chu+=i
	elif '0' <= i <= '9':
		so+=i

print(chu)
print(so)