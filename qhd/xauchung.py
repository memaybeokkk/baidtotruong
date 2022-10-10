s1 = 'Ky thi hoc sinh gioi tinh mon tin hoc'
s2 = 'hoc sinh gioi mon tin hoc'
max = 0
for i in range(len(s1)):
	for j in range(i,len(s1)):
		if s1[i:j+1] in s2:
			if len(s1[i:j+1]) > max:
				max = len(s1[i:j+1])
print(max)