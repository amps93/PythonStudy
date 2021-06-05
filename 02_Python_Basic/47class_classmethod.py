#클래스 메소드 : self를 통하지 않고 바로 클래스가 메소드 호출
#인스턴스를 통하지 않고 클래스에서 바로 호출하여 사용
#첫번째 매개변수에 cls를 지정
#@classmethod

class Person:
    count = 0
    def __init__(self,name):
        Person.count += 1
        self.name = name

    @classmethod
    def print_count(cls):
        print('%d명 태어났습니다'%cls.count) #cls로 클래스 속성에 접근

    def greeting(self):
        print('%s가 인사해요'%self.name)

kim = Person('kim')
Person.print_count()
Lee = Person('Lee')
Person.print_count()
kim.greeting()
Lee.greeting()
