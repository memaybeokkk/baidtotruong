from math import sqrt
s = [int(i) for i in input().split()]
a = []
for i in s:
    if i > 10 and i < 20:
        a.append(i)
print(sum(a))
        
        
