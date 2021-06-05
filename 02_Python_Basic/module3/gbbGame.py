from random import randint

def gbb_game(you_n):
    com = randint(1,4)
    x= com - you_n
    if you_n == com:
        print('비겼습니다')
    elif (x==-2 or x==1):
        print('COM이 이겼습니다')
    else:
        print('당신이 이겼습니다')
    return com

def input_num():
    a = int(input('YOU 입력 (1:가위 2:바위 3:보) : '))
    print('Com Num : %d'%gbb_game(a))
