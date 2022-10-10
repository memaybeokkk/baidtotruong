n =int(input())
for i in range(n):
	for j in range(1,n+1):
		if (j+i) % 2 == 1:
			print('W',end='')
		else:
			print('B',end='')
	print()