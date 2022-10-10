k, a, b, v = [int(i) for i in input().split()]
i = (a -1) //v + 1
j = (i -1) //k + 1
if i - j <= b:
	print(j)
else:
		print(i-b)