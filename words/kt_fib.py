a = [4,7,1,5,1,3,6,8]
def f(n):
    lst = []
    if n != 0:
        a = f(n-1) + f(n-2)
        lst.append(a)
    return lst

fl = f(max(a))
a1 = set(a)
for i in range(0,len(a1))
    for j in range(0,len(f1)):
        if a1[i] == f1[j]:
            

'''
def f(n):
    f = [1,1]
    lst= []
    for i in range(0,len(a)-1):
        for j in range(max(n[i])-1):
            f =
''