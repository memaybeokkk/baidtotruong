s = ['Thấy  rét ,u tôi bọc lại mền','Cô nàng cất rượu ủ thêm men .']
for i in range(len(s)):
	s[i] = s[i].replace('  ',' ')
	s[i] = s[i].replace(' , ',', ')
	s[i] = s[i].replace(' .','.')
	s[i] = s[i].replace(' !','! ')
	s[i] = s[i].replace(' ?','? ')
	s[i] = s[i].replace(' ;','; ')
	s[i] = s[i].replace(' )',') ')
	s[i] = s[i].replace(' (',' (')
print(s)