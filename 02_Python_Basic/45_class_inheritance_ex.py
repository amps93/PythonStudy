#슈퍼클래스 : 사람 클래스 Person
#서브클래스 : 학생클래스 Student

class Person:
    def __init__(self,age,name,sex):
        self.age = age
        self.name = name
        self.sex = sex

    def greeting(self):
        print('안녕하세요')

class Student(Person):
    #학교 학과 학번 공부하다 시험보다
    def __init__(self,age,name,sex,school,major,num):
        super().__init__(age,name,sex)
        self.school = school
        self.major = major
        self. num =num

    def Study(self):
        print('공부하는중')

    def Exam(self):
        print('시험보는중')

a = Student(10,'Kim','M','Hansol','statistics',12345789)
print(a.major)
print(a.school)
print(a.num)
# a.greeting()
a.Study()
a.Exam()