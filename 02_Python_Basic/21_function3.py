# def showInfo(name,age):
#     print('이름은 %s이고 나이는 %d입니다'%(name,age))
#
# showInfo('강민규',29)
#
# def getArea(width, height):
#     return width*height/2
#
# width = int(input('밑변 : '))
# height = int(input('높이 : '))
# print(getArea(width,height))

# def add(a,b):
#     return a+b
#
# def sub(a,b):
#     return a-b
#
# def mul(a,b):
#     return a*b
#
# def div(a,b):
#     return a/b
#
# a = int(input('숫자 1 : '))
# b = int(input('숫자 2 : '))
# print('%d+%d=%d'%(a,b,add(a,b)))
# print('%d-%d=%d'%(a,b,sub(a,b)))
# print('%d*%d=%d'%(a,b,mul(a,b)))
# print('%d/%d=%d'%(a,b,div(a,b)))

def order(price, qty):
    discount = 0
    total = 0
    amount = price * qty
    if amount >= 100000:
        discount = amount * 0.1
    elif amount >= 50000:
        discount = amount * 0.05
    else:
        discount = 0
    total = amount-discount
    return amount, discount, total

orders = order(20000,5)
print('주문액 : %d원\n할인액 : %d원\n지불액 : %d원'%(orders[0],orders[1],orders[2]))
print('-'*50)

orders = order(10000,5)
print('주문액 : %d원\n할인액 : %d원\n지불액 : %d원'%(orders[0],orders[1],orders[2]))
print('-'*50)

orders = order(1000,10)
print('주문액 : %d원\n할인액 : %d원\n지불액 : %d원'%(orders[0],orders[1],orders[2]))
print('-'*50)

#format 사용해서 천단위마다 , 찍기
orders = order(1000,10)
print('주문액 : %s원'%format(orders[0],',').rjust(10))
print('할인액 : %s원'%format(orders[1],',').rjust(10))
print('지불액 : %s원'%format(orders[2],',').rjust(10))
print('-'*50)