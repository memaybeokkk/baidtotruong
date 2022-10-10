a = [int(i) for i in input().split()]
if a[0]>a[1] and a[0]>a[2]:
	print('AN')
elif a[1]>a[0] and a[1]>a[2]:
	print('VINH')
elif a[2]>a[0] and a[2]>a[1]:
	print('Quang')
else:
	print('Bau Lai')
