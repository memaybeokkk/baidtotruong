n = int(input())
a = [int(i) for i in input().split()]
def uocso(x):
	dem = 1
	for i in range(1,x//2 + 1):
		if x % i == 0:
			dem+=1
	return dem
for i in a:
	if uocso(i) == 3:
		print('YES')
	else:
		print('NO')