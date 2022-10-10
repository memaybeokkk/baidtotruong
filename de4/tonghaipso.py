a= int(input())
b= int(input())
c= int(input())
d= int(input())
tu =  a*d + c*b
mau = b + d 
def ucln(a,b):
	if a%b == 0:
		return b
	return ucln(b,a%b)
x = ucln(tu,mau)
tu = tu / x
mau = mau / x
print(tu,mau)