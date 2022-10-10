s1 = 'aba'
s2 = 'bababababa'
i = 0
dem = 0
while i < len(s2)-2:
	if s1 == s2[i:i+3]:
		dem = dem + 1
		i = i + 2
	else:
		i = i + 1
print(dem)
