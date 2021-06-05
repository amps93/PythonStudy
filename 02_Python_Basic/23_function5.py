#함수 내에 사용되는 변수 : local variable(지역 변수)

def show():
    a = 'Hello'
    print(a)

def show1(a):
    print(a)

def show2():
    print(a)

def show3(): #전역변수 a를 변경하고 싶다
    global a
    a = a+'H'
    print(a)

a = 'Hi'
# show()
# show1(a)
# print(a)
show3()

#실습문제
def sub(x,y):

    a = 7
    x,y=y,x
    b=3
    print(a,b,x,y)

a,b,x,y = 1,2,3,4
sub(x,y)
print(a,b,x,y)

def showList(mylist):
    mylist[0]=100
    print(mylist)

mylist = [1,2,3,4]
showList(mylist)
print(mylist)

#딕셔너리 list를 dictionary로 변환
def getProduct(prdList):
    name = prdList['name']
    price = prdList['price']
    return {'name':name,'price':price}

productL = [{'name':'notebook','price':1200000,'maker':'삼성'},
            {'name':'SmartPhone','price':1000000,'maker':'삼성'},
            {'name':'TV','price':2200000,'maker':'LG'},
            {'name':'Air conditioner','price':1800000,'maker':'삼성'}]

for product in productL:
    prdInfo = getProduct(product)
    print(prdInfo)