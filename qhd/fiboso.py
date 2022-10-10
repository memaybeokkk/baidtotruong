def fiboso(n):
	x = 'a'
	y = 'b'
	for i in range(2,n):
		s = y + x 
		x = y
		y = s
	return s
print(fiboso(6))