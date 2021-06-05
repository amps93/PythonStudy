#1
a=[]
for i in range(3):
    a.append(input('회원 입력 : '))
print('회원 명단 : ',*a)

#2
a= int(input('학생 수 입력 : '))
b=[]
for i in range(1, a+1):
    b.append(int(input('학생%d 점수 입력 : '%(i))))

total = 0
for i in range(len(b)):
    total += b[i]
print('총점 : %d'%total)
print('평균 : %d'%(total/a))
c=[]
for i in range(len(b)):
    if b[i]>=80:
        c.append(i)
print('80점 이상 학생 : %d명'%len(c))

#3
a=[]
while True:
    b = input('상품 등록 (엔터키 누르면 종료) : ')
    if b == '':
        break
    a.append(b)
print('등록된 상품 : ',*a)