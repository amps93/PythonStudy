# class Car:
#     #메소드 정의
#     def show(self):
#         print('시험중입니다')
#
# #인스턴스 생성
# car1 = Car()
# car1.show()
# car2 = Car()
# car3 = Car()
# car2.show()
# car3.show()
#
# print(isinstance(car1,Car))
# print(isinstance(car1,int))

#필드 추가 : 메소드 내에서 사용
class Car:
    def show(self):
        print('시험중입니다')
    # def drive(self):
    #     self.speed = 60  #speed 필드
    #     print('%d로 주행중'%self.speed)

    def drive(self, speed):
        self.speed = speed  #speed 필드
        print('%d로 주행중'%self.speed)
#메인 : 인스턴스를 생성하고 이용
car1 = Car()
car1.drive(70)
print(car1.speed)
car1.drive(50)

#인스턴스.필드
car1.color = 'red'
print(car1.color)

print('-'*85)
class Car:
    speed = 0
    color =''
    model = ''

    def show(self):
        print('시험중입니다.')

    def drive(self):
        print('%d로 주행'%self.speed)

mycar = Car()
print(mycar.speed)
mycar.drive()
mycar.speed = 60
mycar.drive()

print('-'*85)
#생성자(constructor) : 인스턴스를 생성해주는 함수
#기본 생성자 : 인스턴스 호출 => 인스턴스면.클래스이름
class Car:
    def __init__(self):
        self.color = 'white'
        self.speed = 0

    def drive(self):
        if self.speed == 0:
            print('정차중입니다')
        else:
            print('%d로 주행중'% self.speed)

    def showInfo(self):
        print('이 자동차의 색상은 %s 입니다'%self.color)

mycar = Car()
print(mycar.color)
print(mycar.speed)
mycar.drive()
mycar.showInfo()

mycar.speed = 90
mycar.drive()


print('-'*85)
#매개변수가 있는 생성자 __init__(self, 매개변수1, 매개변수2, ...):
#-> 필드의 초기값 지정
class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def drive(self):
        if self.speed == 0:
            print('정차중입니다')
        else:
            print('%d로 주행중'% self.speed)

    def showInfo(self):
        print('이 자동차의 색상은 %s 입니다'%self.color)

mycar = Car('red',10)
print(mycar.color)
print(mycar.speed)
mycar.showInfo()
mycar.drive()
mycar.speed = 50
mycar.drive()
print('------------yourcar--------------')
yourcar = Car('blue', 0)
yourcar.showInfo()

print('-'*85)
class Car:
    def __init__(self, speed=0, color='white'):
        self.color = color
        self.speed = speed

    def drive(self):
        if self.speed == 0:
            print('정차중입니다')
        else:
            print('%d로 주행중'% self.speed)

    def showInfo(self):
        print('이 자동차의 색상은 %s 입니다'%self.color)

car1 = Car()
car2 = Car(color='yellow')
car3 = Car(100,'blue')
car4 = Car(10)
car1.showInfo()
car2.showInfo()
car3.showInfo()
car4.drive()

print('-'*85)
#
class Car:
    def __init__(self, speed=0, color='white'):
        self.color = color
        self.speed = speed

    def __str__(self):
        pass

    #color 필드값 반환
    def getColor(self):
        return self.color

    #color 필드 값을 변경
    def setColor(self, color):
        self.color = color

    def drive(self):
        if self.speed == 0:
            print('정차중입니다')
        else:
            print('%d로 주행중'% self.speed)

    #비공개 메서드
    def __showColor(self):
        print('이 자동차의 색상은 %s 입니다'%self.color)

    def showInfo(self):
        self.__showColor()
        print('속도는 %d입니다'%(self.speed))

    def upSpeed(self, up):
        self.speed += up

    def downSpeed(self, down):
        self.speed -= down


car1 = Car()
print(car1.getColor())
car1.setColor('red')
print(car1.getColor())

# car1.__showColor()  #접근 안됨(비공개 메서드라)
car1.showInfo()

car1.upSpeed(4)
car1.drive()
car1.upSpeed(100)
car1.drive()
car1.downSpeed(10)
car1.drive()