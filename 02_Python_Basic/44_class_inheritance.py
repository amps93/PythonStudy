#상속 inheritance
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

class Truck(Car):
    def __init__(self, speed, color, load):
        super().__init__(speed, color) #부모 객체 사용
        self.load = load  #Truck 클래스만의 필드 추가

    #메소드를 재정의 : 오버라이딩(overriding)
    def showLoad(self):
        print(self.load)

    def upLoad(self,up):
        self.load += up

    def showInfo(self):
        print('속도는 %d이고 적재량은 %d입니다'%(self.speed,self.load))

class SportCar(Car):
    def __init__(self,speed,color,seats):
        super().__init__(speed,color)
        self.seats = seats

    def showInfo(self):
        print('SportCar : 색상은 %s, 좌석수는 %d'%(self.color,self.seats))

car1 = Car()
car2 = Truck(100,'blue',1000)

car1.showInfo()
car2.showInfo()
car2.showLoad()

car2.upSpeed(10)
car2.showInfo()

car3 = SportCar(0,'Red',2)
car3.showInfo()

# print(isinstance(car2,Car))
# print(issubclass(Truck,Car))

print('---------polymorphism-------------')
#다형성 polymorphism : 동일한 이름의 메소드이지만 다른 기능을 수행
carL = [car1,car2,car3]

for car in carL:
    car.showInfo()