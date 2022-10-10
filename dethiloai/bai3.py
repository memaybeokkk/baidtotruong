dem = 0
n = input()
while n != 6174 and n != 0:
	s = str(n)
	n1=sorted(s,reverse=True)
	n2=sorted(s)
	s1 = ''.join(n1)
	s2 = ''.join(n2)
	n = int(s1) - int(s2)
	dem+=1
print(n,dem)