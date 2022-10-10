n = int(input())
a = [int(i) for i in input().split()]
s = a.count(100)
if s % 2 == 0:
	print('YES')
else:
	print('NO')



