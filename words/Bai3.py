from math import sqrt
a,b,c = [int(i) for i in input('Nhap a, b, c :').split()]
if a == 0:
    if b == 0:
        if c == 0:
            print('Pt co vo so nghiem')
        else:
            print('Pt vo nghiem')
    else:
        print('Pt co 1 nghiem la :',-c /b)
else:
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + sqrt(d)) / (2*a)
        x2 = ( -b - sqrt(d)) / (2*a)
        print('Pt co 2 nghiem phan biet',round(x1,2),round(x2,2))
    elif d == 0:
        x = -b / (2*a)
        print('Pt co nghiem kep', round(x,2))
    else:
        print('Pt vo nghiem')

