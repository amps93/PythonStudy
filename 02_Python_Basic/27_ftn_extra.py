#재귀함수
# def selfCall():
#     print('ha',end='')
#     selfCall()
#
# selfCall()

#자연수를 입력받으면 해당하는 자연수까지 출력
def count(num):
    print(num,end=' ')
    if num ==2:
        return 1
    return count(num-1)

print(count(5))

#내부함수 : 함수 내에서 정의된 함수
def outFunc(x,y):
    def inFunc(a,b):
        return a+b
    return inFunc(x,y)

print(outFunc(10,20))
# print(inFunc(10,20)) #오류

#lambda
def hap(x,y):
    return x+y
print(hap(10,50))
print((lambda x,y:x+y)(10,50))

hap2=lambda x,y:x+y
print(hap2(5,10))


def hap(x=10,y=20):
    return x+y

print(hap())
print(hap(30,100))

hap3 = lambda x=10,y=20 : x+y
print(hap3())
print(hap3(9,10))

#람다함수 안에서 변수를 생성할 수 없다

#람다함수 list 사용
#리스트의 값에 각각 10을 더하는 람다함수를 작성

# 입력된 값에 10을 더하는 함수
def addTen(x):
    return x + 10

myL = [1,3,4]
print(list(map(addTen,myL))) #맵 활용해서 함수 사용

print(list(map(lambda x:x+10,myL))) #람다사용


#두개의 리스트의 같은 요소의 값들을 더해서 하나의 리스트로 반환
#1) def 함수 정이
#2) lambda 표현식 정의
list1 = [1,2,3,4]
list2 = [10,20,30,40]

def addList(x,y):
    list3 = []
    for i in range(len(list1)):
        list3.append(x[i] + y[i])
    return list3
print(addList(list1,list2))

a = lambda x,y:x+y
print(list(map(a,list1,list2)))

list1 = [1,2,3,4]
list2 = [10,20,30,40]

# 1) def 함수정의
def addList(x,y):
    answer = [x+y for x,y in zip(x,y)]
    return answer
print(addList(list1,list2))

# 2) Lambda 표현식정의
print([(lambda x: x[0]+i[1])(i) for i in zip(list1,list2)])

