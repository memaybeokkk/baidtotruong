a = input()
S1 = [chr(i) for i in range(ord('A'),ord('Z')+1)]
S2 = [chr(i) for i in range(ord('a'),ord('z')+1)]
d1 = 0
d2 = 0
for i in s1:
    if a.count(i) > 0:
        d1 += 1

for i in s2:
    if a.count(i) > 0:
        d2 += 1
a2 = set(a)
print(len(a2))
