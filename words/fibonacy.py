def f(n):
    lst = []
    if n != 0:
        a = f(n-1) + f(n-2)
        lst.append(a)
    return lst
print(f(20))


