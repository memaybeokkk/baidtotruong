s = 'aaahhhhbcdefefbcd'
a1 = []
a2 = []
for i in range(len(s)):
	if s[i] not in a1:
		a1.append(s[i])
		a2.append(s.count(s[i]))
max = 0
for i in range(len(a2)):
	if a2[i] > max:
		max = a2[i]
		vt = i
print(len(a1),a1[vt],max)
