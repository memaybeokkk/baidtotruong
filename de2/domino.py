n = int(input())
s = input()
s1 = s.lstrip('.')
s2 = s.rstrip('.')
d = 0
if s1[0] == 'R':
	d = d + (len(s) - len(s1))
if s2[-1] == 'L':
	d = d + (len(s) - len(s2))
i = 0
s = s1.rstrip('.')
while i < len(s)-1:
	while s[i] != '.' and i < len(s)-1:
		i+=1
	vtd = i - 1
	dem = 0
	while s[i] == '.':
		i+=1
		dem+=1
	vtc = i
	if s[vtd] == 'R' and s[vtc] == 'L':
		d = d + dem % 2
	elif s[vtd] == 'L' and s[vtc] == 'R':
		d = d + dem
	
print(d)