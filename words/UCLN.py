import time
tb = time.time()
#a,b = [int(i) for i in input().split()]
a = 2674
b = 28
def UCLN(a,b):
    du = a % b
    while du != 0:
        a = b
        b = du
        du = a % b
    return b
print(UCLN(a,b))
print(time.time() - tb)
        
from math import gcd
print(gcd(128,64))

