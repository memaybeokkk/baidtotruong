s = input()
s = s.upper()
t = ''
for i in s:
	t = t + str(ord(i))
print(int(t))