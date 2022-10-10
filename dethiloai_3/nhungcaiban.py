n = int(input())
a = [int(i) for i in input().split()]
d = 0
t = 0
for i in range(len(a)):
	if a[i] == 3:
		d+=1
	elif a[i] != 3:
		t = t + a[i]
		if t == 3:
			d+=1
			t = 0
		elif t == 4:
			d+=2
			t = 0
print(d)
