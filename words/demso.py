s = input()
i = 0
n = len(s) - 1 
a = []
while i <= n:
	t = ''
	while i <= n and '0' <= s[i] <= '9':
		t+= s[i]
		i+= 1
	if t != '':
		t.lstrip('0')
		a.append(int(t))
	i+=1
print(a)