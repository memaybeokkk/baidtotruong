n = [i for i in input().split()]
n[0] = n[0][::-1]
n[1] = n[1][::-1]
if int(n[0]) > int(n[1]):
	print(n[0].lstrip('0'))
else:
	print(n[1].lstrip('0'))