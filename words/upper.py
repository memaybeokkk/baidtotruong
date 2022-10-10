S1 = [chr(i) for i in range(ord('A'),ord('Z')+1)]
S2 = [chr(i) for i in range(ord('a'),ord('z')+1)]
C = 
a = input()
for i in S1:
    b = a.count(i)
    if b != 0:
        print(i,b)

for i in S2:
    b = a.count(i)
    if b != 0:
        print(i,b)
    
list()
