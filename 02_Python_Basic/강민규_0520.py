#1-1
for i in range(5,0,-1):
    print('*'*i)
print('-'*50)

#1-2
for i in range(1,6):
    print(' '*(5-i),'*'*(2*i-1))
print('-'*50)
#2
while(True):
    a = int(input('숫자를 입력하세요 : '))
    if a==7:
        print('정답!')
        break
print('-'*50)
#3
cash = 10000
cnt = 0
while cash:
    cash -= 2000
    cnt += 1
    print('노래를 %d번 불렀습니다.'%cnt)
    print('현재 %d원 남았습니다.'%cash)
    if cash==0:
        print('잔액이 없습니다. 종료합니다')