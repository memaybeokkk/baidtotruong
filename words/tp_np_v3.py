#n = int(input())
def TPNP(n):
    a = ''
    while n > 0:
        a+=str(n%2)
        n = n//2
    return a[::-1]
def NPTP(s):
    a = 0
    for i in str(s):
        a = a*2 + int(i)
    return a
def TPHX(n):
    S = ''
    while n > 0:
        du = str(n%16)
        if du == '10':
            S+='A'
        elif du == '11':
            S+='B'
        elif du == '12':
            S+='C'
        elif du == '13':
            S+='D'
        elif du == '14':
            S+='E'
        elif du == '15':
            S+='F'
        else:
            S = S + du
        n = n//16
    return S[::-1]

print(TPHX(999))
