#1
def print_coin():
    print('비트코인')

#2
print_coin()

#3
# for i in range(101):
#     print_coin()
#
# #4
# def print_coins():
#     for i in range(101):
#         print('비트코인')
# print_coins()

#5
# hello()
# def hello():
#     print('Hi')
# hello() 함수가 정의되기 전에 hello()를 먼저 불러와서

#6
# A
# B
# C
# A
# B

#7
# A
# A
# C
# B

#8
# A
# C
# A
# E
# D

#9
# B
# A

#10
# B
# C
# B
# C
# B
# C
# A

#11
# def mul(a,b):
#     return a*b
# print(mul(10,15))
#
# #12
# def upper(a):
#     return a.upper()
# print(upper('ticker'))
#
# #13
# def pickup_even(a):
#     b=[]
#     for i in a:
#         if i%2==0:
#             b.append(i)
#     return b
#
# print(pickup_even([1,2,3,4,5,6,7,8,9,10]))

def sootja():
    e=[]
    while 1:
        n = input('숫자를 입력하세요.(엔터키 누르면 종료) : ')
        if n=='':   #엔터키 누르면 종료하게 하는것
           break
        else:
           e.append(int(n))
    return e


def pickup_even():
    e = sootja()
    f=[]
    for i in e:
        if i % 2==0 :
            f.append(i)
        # else:
        #     continue
    return f

print(pickup_even())
