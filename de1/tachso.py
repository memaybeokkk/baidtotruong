s = input()
a = []
i = 0
"""while i < len(s):
	t = ''
	if '0' <= s[i] <= '9':
		t+=s[i]
	else:
		if t!='':
			a.append(t)
			t=''
	i+=1
print(a)"""

while i < len(s):
	t = ''
	while '0' <= s[i] <= '9':
		t+= s[i]
		i+=1
		if i == len(s):
			break
	if t!='':
		a.append(int(t.lstrip('0')))
	i+=1
for i in a:
	print(i,end=' ')
a.sort()
print()
for i in a:
	print(i,end=' ')