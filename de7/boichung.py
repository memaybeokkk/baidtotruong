from math import lcm
a = 'AAABDA'
b = [0] * 123
for i in a:
	b[ord(i)]= b[ord(i)] + 1
max = 0
for i in range(len(b)):
	if b[i] != 0 and b[i] > max:
		max = b[i]
s = lcm(max,100000)
print(s)