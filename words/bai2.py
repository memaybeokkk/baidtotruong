from math import sqrt
a,b,c = [int(i) for i in input('Nhap do dai cac canh: ').split()]
Cv = a + b + c
P = Cv / 2
S = sqrt(P*(P-a)*(P-b)*(P-c))
h1 = (2*S)/a
h2 = (2*S)/b
h3 = (2*S)/c
if (a == b) or (a == c) or (b == c):
    print('Day la tam giac can')
if (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == a**2 + b**2):
    print('Day la tam giac vuong')
print(round(h1,2))

