def uoc_so(x):
	t = 0
	for i in range(1,x//2 + 1):
		if x % i == 0:
			t+=i
	return t 

for i in range(100,1001):
	if i == uoc_so(uoc_so(i)):
		print(i,uoc_so(i))



