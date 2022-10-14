a = 1
b = 1000000
c = [0] * 10
import collections 
for i in range(a,b+1):
	d = str(i)
	for j in d:
		c[int(j)]+=1
'''
t=[x for x in t]
t= collections.Counter(t)
print(t)
'''
print(c)
'''
word = "mississippi"

counter = {}

for letter in t:
	if letter not in counter:
		counter[letter] = 0
	counter[letter] += 1
'''