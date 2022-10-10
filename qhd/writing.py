import itertools
a = 'c A d a'
a = a.split()
b = []
s = 'AbrAcadAbRa'
dem = 0
for i in itertools.permutations(a):
	b.append(''.join(i))
for i in range(len(s)):
	if s[i:i+len(a)] in b:
		dem+=1
print(dem)