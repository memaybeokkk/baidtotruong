from math import sqrt
n = int(input('Nhap so nguyen: '))
Kt = True 
if n % 2 == 0:
    print('Day la so chan')
else:
    print('Day la so le')
for i in range(2,int(sqrt(n)+ 1)):
    if n % i == 0 or n == 1:
        Kt = False
        print('day khong phai la so nguyen to')
        break
if Kt == True:
    print('Day la so nguyen to')
a = []
for i in range(1,int(n/2) + 1):
    if n % i == 0:
        a.append(i)
if sum(a) == n:
    print('day la so hoan hao')
else:
    print('day khong phai la so hoan hao')
