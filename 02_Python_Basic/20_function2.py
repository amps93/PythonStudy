# def get_triangle_area():
#     a = int(input('높이 : '))
#     b = int(input('밑변 : '))
#     return('높이 : %d\n밑변 : %d\n삼각형의 면적:%d'%(a,b,((a*b)/2)))
#
# t = get_triangle_area()
# print(t)

def get_triangle_area(height, width):
    return('높이 : %d\n밑변 : %d\n삼각형의 면적:%d'%(height,width,((height*width)/2)))

t = get_triangle_area(10,5)
print(t)


def order():
    a = int(input('상품 가격 입력 : '))
    b = int(input('주문 수량 입력 : '))
    return a, b, a*b

orders = order()
print('상품가격 : %d원\t주문수량 : %d원\t주문액 : %d원'%(orders[0],orders[1],orders[2]))

#리스트 반환값
def getNames():
    names=[]
    for i in range(3):
        name = input('이름 입력 : ')
        names.append(name)
    return names

nameL = getNames()
print(nameL)

#이름과 나이를 입력받아 딕셔너리 형식으로 변환
def getNames2():
    names={}
    name = input('이름 입력 : ')
    age = int(input('나이 입력 : '))
    names = {'name':name,'age':age}
    return names

nameD = getNames2()
print(nameD)