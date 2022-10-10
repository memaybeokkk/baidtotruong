a, b = [i for i in input().split()]
s = 0
for i in a:
	for j in b:
		s = s + int(i)*int(j)
print(s)