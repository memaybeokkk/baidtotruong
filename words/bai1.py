a = int(input())
b = 0
for i in range(0,a):
    if i % 2 == 0:
        b += 1
        print(i, end='   ')
    if b == 15:
        print('\n')
        b = 0
        
    
    
