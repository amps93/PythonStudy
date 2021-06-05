def area_square(width, height):
    a=0
    area = width*height
    return area

w = 10
h = 20
area = area_square(w,h)
print(area)

def printName(name):
    print(name)

printName("Lee")

def printHello():
    print('Hello')

printHello()

def sum():
    a = int(input('숫자1 : '))
    b = int(input('숫자2 : '))
    return (a+b)

res = sum()
print('합은 %d' % res)
print('합은 %d'%sum())