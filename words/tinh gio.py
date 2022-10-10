h,m,s = [int(i) for i in input('Nhap lan luot so gio, phut, giay: ').split(sep=': ')]
print(h,m,s)
bs = s + int(input('Nhap so giay them vao: '))
s1 = bs % 60
s2 = bs // 60
m = m + s2
m1 = m % 60
m2 = m // 60
h = h + m2
print(h,m1,s1,sep=': ')
