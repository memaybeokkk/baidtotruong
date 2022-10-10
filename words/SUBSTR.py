with open('SUBSTR.INP','r') as tep1:
	k = int(tep1.readline())
	s = tep1.readline()
dem = d = 0
for i in range(0,len(s)):
	d = 0
	for j in range(i,len(s)):
		if s[j] == '1' and d < 2:
			d+=1
			if d == k:
				dem+=1
			elif d > 2:
				break
		if d == k and s[j] == '0':
			dem+=1
print(dem)
with open('SUBSTR.OUT','w') as tep2:
	tep2.write(str(dem))