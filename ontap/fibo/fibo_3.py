a = [8,1,1,7,1,1,2]
#    0,1,2,3,4,5,6
i = 0
dmax = 0
d = 0
n = len(a)
j = 0
while i < n - 2:
    if a[i] == a[i+1] == 1:
        j = i + 2
        while a[j] == a[j - 1] + a[j - 2]:
            j = j + 1
            if j >= n:
                break
        d = j - i
        if d > dmax:
            dmax = d
            vtd = i
            vtc = j
        i = j
    else:
        i+=1
    print(i)

print(a[vtd:vtc])