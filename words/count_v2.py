a = [int(i) for i in input().split()]
b = [0]*(max(a)+1)
for i in a:
    b[i] = b[i] + 1
for i in range(0,(max(a)+1)):
    if b[i] != 0:
        print(i,b[i])
