def openBox():
    global count
    print('박스열기')
    count -= 1
    if count == 0:
        print('###반지넣기###')
        return

    openBox()
    print('박스닫기')

count = 10

openBox()

def addNum(num):
    if num <= 1:
        return 1
    return num + addNum(num-1)

print(addNum(10))

def factorial(num):
    if num == 1:
        return 1
    return num*factorial(num-1)

print(factorial(5))