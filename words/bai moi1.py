from math import sqrt
def SNT(n):
    Kt = True
    for i in range(2,int(sqrt(n)+ 1)):
        if n % i == 0 or n == 1:
            Kt = False
            return Kt
    return Kt
        
for i in range(100):
    if SNT(i):
        print(i)
