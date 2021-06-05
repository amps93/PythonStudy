#타입 변환
print('나는 현재 나이가 '+ str(23) +'살 입니다')
print('나는 현재 나이가 {}살 입니다'.format(str(23)))
print('나는 현재 나이가 {0}살 입니다'.format(str(23)))
print('나는 현재 나이가 {0}살 이고 키는 {1:10.2f}입니다'.format(23,176.25))
print('나는 현재 나이가 %d살 입니다'%23)

# num = input('숫자를 입력하세요 : ')
# print(type(num),type(int(num)))

# print(float(num)+100)

#두개의 수를 입력 받아 두 수의 합과 평균 구하기
a=int(input('숫자 입력1'))
b=int(input('숫자 입력2'))

sum = a+b
mean = (a+b)/2
print(sum,mean)