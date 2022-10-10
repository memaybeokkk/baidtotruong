def songay(m,y):
	m = int(m)
	y = int(y)
	m1 = [1,3,5,7,8,10,12]
	m2 = [4,6,9,11]
	if m in m1:
		return 31
	elif m in m2:
		return 30
	else:
		if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
			return 29
		else:
			return 28
def sau(d,m,y,n):
	d = d + n
	while d > songay(m,y):
		d = d - songay(m,y)
		m = m + 1
		if m > 12:
			m = 1
			y+= 1
	return d,'/',m,'/',y
def truoc(d,m,y,n):
	d = d - n
	while d <= 0:
		m = m - 1 
		d = songay(m,y) - abs(d)
		if m == 1:
			m = 12
			y = y - 1
	return d,'/',m,'/',y
a = truoc(3,10,2022,37)
print(a)