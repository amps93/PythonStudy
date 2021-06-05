#eval() : 입력된 문자열에 해당하는 숫자형으로 변환
'''
num1 = eval(input('number1 : '))
num2 = eval(input('number2 : '))
print(type(num1))
print(type(num2))
total = num1+num2
print('합은 {}'.format(total))
'''

print(eval(input()))  #3+2 입력


#5000원으로 120원짜리 사탕을 몇개 살수 있고 남은돈은 얼마인가
a=5000
b=120
print('사탕 개수 : %d'%(5000//120))
print('남은돈 : %d'%(5000%120))