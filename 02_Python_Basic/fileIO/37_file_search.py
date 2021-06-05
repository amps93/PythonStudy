#read()함수 이용하여 원하는 내용이 파일에 있는지 검색

value = input('검색값 입력 : ')
f= open('test3.txt','r',encoding='utf-8')
data = f.read()

if value in data:
    print('있다')
else:
    print('없다')


f.close()