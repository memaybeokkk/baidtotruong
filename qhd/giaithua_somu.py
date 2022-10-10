n = int(input())
def daybinhphuong(n):
	s = 0
	for i in range(1,n+1):
		s = s + i**2
	return s
def daypsbphuong(n):
	s = 2000
	for i in range(1,n+1):
		s = s + 1/i**2
	return s
def gthua(n):
	if n == 1:
		return 1
	elif n == 0:
		return 0
	return gthua(n) * gthua(n-1)
def daygiaithua(n):
	s = 0
	for i in range(1,n+1):
		s = s + gthua(i)
	return s
def daygiaithuachan(n):
	s = 0
	for i in range(2,n**2+1,1):
		s = s + gthua(i)
	return s
def daygiaithuale(n):
	s = 0
	for i in range(1,n**2+2,1):
		s = s + gthua(i)
	return s
print(gthua(1))