#1
a= input('16진수 한글자 입력 : ')

if a == 'A':
    print('10진수 ==> %d'%10)
elif a=='B':
    print('10진수 ==> %d'%11)
elif a=='C':
    print('10진수 ==> %d'%12)
elif a=='D':
    print('10진수 ==> %d'%13)
elif a=='E':
    print('10진수 ==> %d'%14)
elif a=='F':
    print('10진수 ==> %d'%15)
else:
    print('16진수가 아닙니다')
print('-'*50)
#2
a=int(input('교환할 돈은 얼마? '))

b=a//50000
a%=50000

c=a//10000
a%=10000

d=a//5000
a%=5000

e=a//1000
a%=1000

f=a//500
a%=500

g=a//100
a%=100

h=a//50
a%=50

i=a//10
a%=10

print('50000원 {0}장, 10000원 {1}장, 5000원 {2}장, 1000원 {3}장\n500원{4}개, 100원{5}개, 50원{6}개, 10원{7}개'.format(b,c,d,e,f,g,h,i))
print('바꾸지 못한 돈 ==> %d'%(a))
print('-'*50)
#3
from random import randint

A = randint(1,7)
B = randint(1,7)
print('A의 주사위는 {}입니다'.format(A))
print('B의 주사위는 {}입니다'.format(B))

if A>B:
    print('A가 이겼다')
elif B>A:
    print('B가 이겼다')
else:
    print('비겼다')