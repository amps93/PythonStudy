crawling = 'Data crawling is fun'
parsing = 'Data parsing is also fun'

print(crawling)
print(parsing)

print(type(crawling))
print(type(parsing))

#in
string = 'Python is cool'
print('python' in string)
print('Python' in string)

if 'Python' in string:
    print("있습니다")
else:
    print('없습니다')

#in과 list
names = ['홍길동','변학도','성춘향','이몽룡']
name = input('input name : ')
if name in names:
    print('있다')
else:
    print('없다')