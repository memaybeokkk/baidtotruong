
def ams(n):
    m = n
    T = 0
    kt = False
    while m > 0:
        du = m % 10
        m = m // 10
        T = T + du**len(str(n))
    if T == n:
        kt = True
    return kt
for i in range(100,999999):
    if ams(i):
        print(i)
