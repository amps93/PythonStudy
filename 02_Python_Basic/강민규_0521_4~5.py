#4
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
b.sort()
print('점수 내림차순 정렬 : ',b)

#5
from random import randint
saja = ["개과천선", "구사일생", "군계일학", "무용지물", "동고동락", "유비무환", "입신양명", "괄목상대", "막역지우", "고장난명"]
meaning = ["잘못을 고치고 옳은 길에 들어섬", "죽을 고비를 여러 번 겪으며 살아나다", "평범한 사람 가운데 뛰어난 사람", "아무짝에도 쓸모없는 것",
           "고통과 즐거움을 함께 한다", "미리 준비해두면 근심 걱정이 없다", "사회적으로 인정받고 출세하여 이름을 세상에 드날림",
           "다른 사람의 학식이나 업적이 크게 진보한 것을 말함", "생사를 같이 할 수 있는 친밀한 벗", "상대 없이 혼자서는 어떤 일을 이룰 수 없다"]

print('사자성어 맞추기 게임을 시작합니다')
print('-'*50)
a = randint(0,9)
while True:
    print(meaning[a])
    b = input('이 말의 사자성어는? : ')
    if b == saja[a]:
        print('맞습니다. 게임을 종료합니다')
        break
    else:
        print('틀렸습니다. 다시 도전\n')
