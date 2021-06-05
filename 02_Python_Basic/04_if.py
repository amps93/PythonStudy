# id = 'flower'
# pw = 1234
#
# a = input('id : ')
# b = int(input('pw : '))
#
# if a == id and b == pw:
#     print('로그인 성공!')
# else:
#     print('로그인 실패!')

a = int(input('도형입력 (1:사각형 , 2:삼각형, 3:원) : '))

if a == 1:
    w = int(input('가로 입력 : '))
    h = int(input('세로 입력 : '))
    print('사각형의 면적 = %d'%(w * h))
elif a == 2:
    w = int(input('밑변 입력 : '))
    h = int(input('높이 입력 : '))
    print('삼각형의 면적 =' %(w * h / 2))
else:
    r = int(input('반지름 입력 : '))
    print('원의 면적 = %f'%(r * r * 3.14))