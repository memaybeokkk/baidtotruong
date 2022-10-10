s = 'hhooocccsssiiiiinnnhhh'
s = list(s)
i = 0
while i <= len(s)-2:
	print(s,i)
	while s[i] == s[i+1]:
		del s[i]
		if i == len(s) - 1:
			break

	i+=1
print(s)