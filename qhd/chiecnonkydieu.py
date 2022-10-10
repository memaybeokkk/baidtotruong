s = '5313525313525313525'
for j in range(len(s)):
	s1 = s[:j]
	s2 = s.replace(s1,'')
	if len(s2) == 0:
		print(len(s1))
		break
	else:
		if s1.find(s2) == 0:
			print(len(s1))
			break
		elif s1.find(s2) == -1:
			kt = False
if kt == False:
	print(len(s))