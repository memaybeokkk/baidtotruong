n = int(input())
a = [int(i) for i in input().split()]
x = int(input())
dem = 0
for i in range(n):
	for j in range(i+1,n):
		if a[i] + a[j] == x:
			dem+=1
print(dem)