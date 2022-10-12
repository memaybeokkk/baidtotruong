a = [chr(i) for i in range(ord('a'),ord('z')+1)]
b = [chr(i) for i in range(ord('A'),ord('Z')+1)]
s = 'Heal the World'
s1 = ''
for i in s:
	if i in a:
		s1+=a[(a.index(i)+5)%26]
	elif i in b:
		s1+=b[(b.index(i)+5)%26]
	else:
		s1+=' '

print(s1)