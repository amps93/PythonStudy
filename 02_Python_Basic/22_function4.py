#default argument는 맨뒤에!

def showInfo(name, age=10,sex='F'):
    print(name, age, sex)

showInfo('홍길동')
showInfo('김학도',40)
showInfo('변학도',45,'M')

def showNames(names):
    for name in names:
        print(name)

names = (['Hong','Park','Chio','Lee'])
showNames(names)

#함수의 실인수로 딕셔너리가 전달
def showInfoStd(student):
    print(student)
    print('이름 : ',student['name'])
    print('나이 : ', student['age'])
    print('연락처 : ', student.get('phone'))

info_std = {'name':'kim','age':19,'phone':'010-0000-0000'}
showInfoStd(info_std)

#가변길이 매개 변수
#*args : argument 1개 이상 지정
#*kwargs : keywordarguments key = value

def mySum(*args):
    total = 0
    for x in args:
        total += x
    return total

print(mySum(1,3,5))
print(mySum(3,4))
print(mySum(1,2,4,5,6))

def myShowInfo(**kwargs):
    for key in kwargs.keys():
        print(key,end=' ')
    print()
    for value in kwargs.values():
        print(value, end= ' ')
    print()
    for item in kwargs.items():
        print(item)

myShowInfo(id=123,name='kim',add='seoul')
myShowInfo(id=333,name='lee')
myShowInfo(id=321,name='hong',add='daegu',phone='010-0000-0000')



def calculator(operator, *args):
    pass

def studentInfo(name, age=4, sex='M'):
    student = {'name':name,
               'age':age,
               'sex':sex
               }
    return student

studentInfo('Lee',30,'F')
print(studentInfo(name='Kim',age=30,sex='M'))
print(studentInfo(name='Kim',sex='M',age=30))

print(studentInfo('Kim',sex='M',age=30)) #가능
# print(studentInfo(name='Kim', 15, 'F')) #불가능
