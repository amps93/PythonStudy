#1
students = [
   {"name" : "홍길동", "korean" : 87, "math" : 98, "english" : 88, "science" : 95},
   {"name" : "이몽룡", "korean" : 92, "math" : 98, "english" : 96, "science" : 98},
   {"name" : "성춘향", "korean" : 76, "math" : 96, "english" : 94, "science" : 90},
   {"name" : "변학도", "korean" : 98, "math" : 92, "english" : 96, "science" : 92},
   {"name" : "박지성", "korean" : 95, "math" : 98, "english" : 98, "science" : 98},
   {"name" : "류현진", "korean" : 64, "math" : 88, "english" : 92, "science" : 92}
]

print('이름  총점  평균')
for i in range(len(students)):
    total = (sum(list(students[i].values())[1:5]))
    avg = total / 4
    print(students[i].get("name"), total, avg)

#2
dictionary = {}
while True:
    Eng = input('영어 단어 등록 (종료는 Quit) : ')
    if Eng == 'Quit':
        break
    if Eng in dictionary:
        print('%s는 이미 등록된 단어입니다.'%Eng)
        continue
    Kor = input('%s의 뜻 입력 : '%Eng)

    dictionary[Eng] = Kor

print(dictionary)

while True:
    search_eng = input('검색할 단어 입력 (종료는 Quit) : ')
    if search_eng == 'Quit':
        break
    if search_eng in dictionary.keys():
        print('%s의 뜻은 %s입니다'%(search_eng, dictionary[search_eng]))
    if search_eng not in dictionary.keys():
        print('%s는 등록되지 않은 단어입니다.'%search_eng)
