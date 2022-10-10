n = int(input())
minx = miny = 100000000
maxx = maxy = 0
for i in range(n):
	x,y,r = [int(i) for i in input().split()]
	if x + r > maxx:
		maxx = x + r + 5
	if y + r > maxy:
		maxy = y + r + 5
	if x - r < minx:
		minx = x - r - 5
	if y - r < miny:
		miny = y - r - 5
print(maxy,maxy)
print(minx,miny)

