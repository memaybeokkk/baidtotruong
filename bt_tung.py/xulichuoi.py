s = 'hsgtinh'
s = s.lower()
na = ['a','o','y','e','u','i']
s1 = []
for i in range(len(s)):
	if s[i] not in na:
		s1.append('.'+s[i])
s1 = ''.join(s1)
		
print(s1)
