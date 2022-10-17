f2 = open('number.OUT','w')
a = []
with open('number.INP','r') as f1:
	n = int(f1.readline())
	for i in range(n):
		s = f1.readline()
		j = 0
		print(s)
		while j < len(s):
			x = ''
			while '0' <= s[j] <= '9' and j < len(s):
				x+=s[j]
				j+=1
			if x != '':
				if x == '0':
					a.append(str(0))
				else:
					a.append(x.lstrip('0'))
			j+=1
print(a)
a = sorted(a,key=len)
for i in a:
	f2.write(i)
	f2.write('\n')
f2.close()

