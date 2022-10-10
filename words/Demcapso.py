a = [int(i) for i in input().split()]
dem = 0
for i in range(1,a[0]+1):
	for j in range(1,a[1]+1):
		if (i + j) % 5 == 0:
			dem+=1
print(dem)