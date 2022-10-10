a = [1,7,9,2,1,6,9,5]
min = a[0]
cs = 0
for i in range(len(a)):
    if a[i] <= min:
        min = a[i]
        cs = i

max = a[0]
csm = 0

for i in a:
    if i > max:
        max = i
        csm = a.index(i)

print(a)
temp = a[cs]
a[cs] = a[csm]
a[csm] = temp

print(a)
